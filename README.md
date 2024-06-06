# Object Finder Bot using Feature Matching and Detection Algorithms

## Introduction

The Object Finder Bot is a Python-based application that utilizes Feature Matching and Detection Algorithms to locate a target object within a reference image. This powerful bot can assist users in identifying specific objects within complex images, making it a valuable tool for various applications such as computer vision, image analysis, and object recognition.

## Features

- User-friendly Graphical User Interface (GUI) built using Tkinter.
- Supports matching a target object against a reference image.
- Utilizes Feature Matching and Detection Algorithms for accurate object identification.
- Displays detailed results, including matched keypoints and bounding box around the target object.
- Provides options for adjusting algorithm parameters to fine-tune the matching process.
- Allows users to load custom target and reference images from their local storage.

## How it Works

The Object Finder Bot uses the following main steps to find the target object in the reference image:

1. **Input**: The user provides the target image and the reference image via the GUI.

2. **Feature Detection**: The bot employs feature detection algorithms, such as SIFT (Scale-Invariant Feature Transform) or ORB (Oriented FAST and Rotated BRIEF), to identify key feature points in both the target and reference images.

3. **Feature Matching**: The bot matches the key feature points between the target and reference images using techniques like Brute-Force Matching, FLANN (Fast Library for Approximate Nearest Neighbors) Matching, or other efficient algorithms.

4. **Filtering and Validation**: The bot filters out incorrect matches and validates the reliable matches based on parameters like distance ratio or homography.

5. **Visualization**: The bot visualizes the matched keypoints and draws a bounding box around the target object in the reference image.

6. **Result Display**: The final result is displayed on the GUI, showing the reference image with the identified target object highlighted.

## Getting Started

Follow these steps to set up and run the Object Finder Bot on your local machine:

1. Clone the repository: `git clone https://github.com/VishalManam//object-detection-bot.git`
2. Navigate to the project directory: `cd object-detection-bot`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python object_detection_bot.py`

## Usage

1. Launch the Object Finder Bot application by executing the `object_detection_bot.py` script.
2. Click on the "Load Target Image" button to load the image of the object you want to find in the reference image.
3. Click on the "Load Reference Image" button to load the image in which you want to search for the target object.
4. Adjust the algorithm parameters (if required) using the sliders or input fields provided in the GUI.
5. Click the "Find Object" button to initiate the feature matching process.
6. The result will be displayed in a new window, showing the reference image with the identified target object highlighted.


## Example Input

![ikigai](https://github.com/VishalManam/object-detection-bot/assets/88299493/f2937028-fe67-435a-a3c3-68e2aa399bd7)

![ikigai and other books](https://github.com/VishalManam/object-detection-bot/assets/88299493/cc5bac66-8168-4b89-93dd-5ac0ab4e1756)

## Example Output

![image1_with_key_points](https://github.com/VishalManam/object-detection-bot/assets/88299493/cf6bc0f8-5534-4338-a892-741c1c5c3923)

![image2_with_key_points](https://github.com/VishalManam/object-detection-bot/assets/88299493/effb1eb5-9c7f-4edb-9972-d40832c1b4f1)

![ikigai_matches](https://github.com/VishalManam/object-detection-bot/assets/88299493/9a5f3b77-b4b9-4374-98de-db062cc3c561)

![ikigai_identified](https://github.com/VishalManam/object-detection-bot/assets/88299493/18dfa751-4f7c-4c7b-980f-5c9ada5e9f98)


## Algorithm Configuration

The Object Finder Bot allows users to fine-tune the feature matching process by adjusting the following algorithm parameters:

- Feature Detector (SIFT, ORB, etc.)
- Matcher (Brute-Force, FLANN, etc.)
- Filtering Thresholds
- Homography Thresholds

## Contributions

Contributions to this project are welcome! If you have any suggestions or improvements, feel free to create a pull request. Please ensure to follow the project's code of conduct.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The bot was inspired by the incredible work in computer vision and object recognition.
- Thanks to the developers of OpenCV, NumPy, and Tkinter for providing powerful libraries for image processing and GUI development.
