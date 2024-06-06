import cv2
import numpy as np
from PIL import Image, ImageEnhance

def alignImages(image1_path, image2_path):
    # Read reference image
    image1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    
    # Read target image
    image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)

    # Convert images to grayscale
    image1Gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2Gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Detect SIFT features and compute descriptors
    sift = cv2.SIFT_create()
    key_points1, descriptors1 = sift.detectAndCompute(image1Gray, None)
    key_points2, descriptors2 = sift.detectAndCompute(image2Gray, None)

    # Init brute-force feature matcher
    matcher = cv2.BFMatcher()

    # Match descriptors firstly using knn, k=2
    matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

    # Apply ratio test to filter only good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Extract keypoint coordinates of good matches for geometric verification
    src_pts = np.float32([key_points1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([key_points2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Perform RANSAC to estimate homography
    homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Apply mask to filter out outliers
    filtered_matches = [m for i, m in enumerate(good_matches) if mask[i]]

    # Draw keypoints on imageReference
    image1_with_key_points = cv2.drawKeypoints(image1, key_points1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    outputFilename1 = r"D:\Downloads\object-detection-bot\image1_with_key_points.jpg"
    cv2.imwrite(outputFilename1, image1_with_key_points)

    # Draw keypoints on image
    image2_with_key_points = cv2.drawKeypoints(image2, key_points2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    outputFilename2 = r"D:\Downloads\object-detection-bot\image2_with_key_points.jpg"
    cv2.imwrite(outputFilename2, image2_with_key_points)

    # Draw matches
    match_img = cv2.drawMatches(image1, key_points1, image2, key_points2, filtered_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    outputFilename3 = r"D:\Downloads\object-detection-bot\matches.jpg"
    cv2.imwrite(outputFilename3, match_img)

    # Use homography to align image wrt imageReference for further comparison
    height, width, channels = image2.shape
    imageReg = cv2.warpPerspective(image1, homography, (width, height))

    # Save the enhanced aligned image
    saveFilename = r"D:\Downloads\object-detection-bot\ikigai_detected.jpg"
    cv2.imwrite(saveFilename, imageReg) #imageReg

    return imageReg, homography

# Usage example
refFilename = r"D:\Downloads\object-detection-bot\ikigai.jpg"  # reference image path
imFilename = r"D:\Downloads\object-detection-bot\ikigai and other books.jpg"  # target image path
aligned_and_enhanced_image, homography = alignImages(refFilename, imFilename)