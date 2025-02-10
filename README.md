# Real-Time Finger Counting System

This project is a **real-time finger counting system** using **OpenCV** and **MediaPipe**. It captures live video from a webcam, detects hand landmarks, and counts the number of extended fingers based on their positions. The live count is displayed on the screen in real time.

## Features
- Detects hand landmarks using **MediaPipe**.
- Counts the number of extended fingers.
- Displays the count on the live video feed.
- Runs in real-time using a webcam.

## Requirements
Make sure you have the following dependencies installed:

```bash
pip install opencv-python mediapipe
```

## Usage
1. Clone this repository or copy the script.
2. Run the script:

```bash
python handtracking.py
```

3. The webcam feed will open, displaying the detected fingers.
4. Press `q` to exit the program.

## Code Explanation
- Captures frames from the webcam using **OpenCV**.
- Converts frames to RGB for MediaPipe processing.
- Detects hand landmarks and checks which fingers are extended.
- Displays the real-time finger count on the screen.

## License
This project is open-source and available for use under the **MIT License**.
