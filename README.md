# 🖐️ Hand Desktop Controller

A simple Python-based desktop controller that allows you to control your computer using hand gestures. This project leverages computer vision techniques with OpenCV, MediaPipe for hand tracking, and PyAutoGUI for system control.

## ✨ Features

*   **Gesture Recognition** 🖐️: Detects and interprets various hand gestures for computer control.
*   **Cursor Control** 🖱️: Move your mouse cursor using hand movements detected by the webcam.
*   **Left Click** 👆: Perform left clicks by pinching your index and middle fingers together.
*   **Scrolling** 🔄: Scroll up or down by raising all five fingers and moving your hand vertically.
*   **Real-time Tracking** ⏱️: Provides immediate feedback and control based on hand movements.
*   **Smooth Cursor Movement** ✨: Implements linear interpolation to reduce cursor jitter for a smoother experience.
*   **Configurable Settings** ⚙️: Allows adjustments for frame reduction, smoothing, and click thresholds.

## 🛠️ Tech Stack

*   **Core Libraries**: OpenCV (`cv2`), MediaPipe, PyAutoGUI, NumPy
*   **Programming Language**: Python 🐍
*   **Hand Tracking**: MediaPipe Hands
*   **System Control**: PyAutoGUI

## 🚀 Installation

To get started with the Hand Desktop Controller, follow these steps:

1.  **Clone the Repository**: 
    ```bash
    git clone https://github.com/rishithkoduri/hand_desktop_controller.git
    cd hand_desktop_controller
    ```

2.  **Install Dependencies**: 
    This project requires several Python packages. You can install them using pip with the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
    This command will install `opencv-python`, `mediapipe`, `pyautogui`, and `numpy`.

3.  **Ensure Webcam is Connected**: 
    Make sure your computer's webcam is connected and accessible.

## 💻 Usage

Once the installation is complete, you can run the application directly from the command line:

1.  **Run the Main Script**: 
    Navigate to the cloned repository directory in your terminal and execute the main Python script:
    ```bash
    python main.py
    ```

2.  **Understanding Gestures**: 
    The application will start, displaying a video feed from your webcam. The following hand gestures are recognized:
    *   **Move Cursor**: Keep your index finger raised (other fingers down). Move your hand to control the cursor.
    *   **Left Click**: Raise your index and middle fingers. When the distance between these two fingers is small (pinch gesture), a left click will be registered.
    *   **Scrolling**: Raise all five fingers. Move your hand up to scroll up and down to scroll down.

3.  **Exiting the Application**: 
    Press the 'q' key while the application window is active to quit.

## ⚙️ Configuration

You can adjust certain parameters in the `main.py` file to fine-tune the controller's behavior:

*   `CAM_WIDTH`, `CAM_HEIGHT`: Set the desired webcam resolution.
*   `FRAME_REDUCTION`: Defines a margin around the webcam feed. Hand movements within this reduced frame control the cursor, making it easier to reach screen edges.
*   `SMOOTHING`: Controls the level of cursor smoothing. Higher values result in smoother movement but may introduce slight lag.
*   `CLICK_THRESHOLD`: Determines the maximum distance between the index and middle fingertips to trigger a click.

## 📂 Project Structure

```plaintext
hand_desktop_controller/
├── main.py             # Main application script for gesture control
├── controller_utils.py # Utility functions for coordinate mapping and smoothing
├── hand_tracker.py     # Class for hand detection and landmark extraction using MediaPipe
├── requirements.txt    # Lists all project dependencies
└── README.md           # Project documentation (this file)
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some YourFeature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

Please ensure your code adheres to the project's style and includes appropriate tests if applicable.


## 🔗 Important Links

*   **Repository**: [https://github.com/rishithkoduri/hand_desktop_controller](https://github.com/rishithkoduri/hand_desktop_controller)
*   **Author**: [rishithkoduri](https://github.com/rishithkoduri)


--- 

© 2023 **hand_desktop_controller**

[Return to Top](#user-content-hand-desktop-controller)

--- 

*   Fork this repository on [GitHub](https://github.com/rishithkoduri/hand_desktop_controller/fork)
*   Star this project if you find it useful ⭐
*   Open an [issue](https://github.com/rishithkoduri/hand_desktop_controller/issues) if you encounter any problems or have suggestions.


---
