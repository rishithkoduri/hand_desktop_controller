# 🖱️ AI Virtual Mouse & Hand Gesture Controller

A Python-based application that allows you to control your desktop mouse cursor and perform actions (clicking, scrolling, dragging) using hand gestures captured by your webcam. This project utilizes computer vision and machine learning to create a touch-free interface.

## ✨ Features

* **Cursor Movement:** Move the mouse pointer by moving your index finger.
* **Left Click:** Pinch your Index finger and Thumb together.
* **Right Click:** Pinch your Middle finger and Thumb together.
* **Double Click:** Quick pinch gesture (configurable).
* **Dragging:** Hold the click gesture and move your hand.
* **Smoothing:** Jitter reduction for precise cursor control.
* **Frame Rate Display:** Real-time FPS monitoring.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Computer Vision:** OpenCV (`cv2`)
* **Hand Tracking:** Google MediaPipe
* **GUI Automation:** PyAutoGUI
* **Math Operations:** NumPy

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.7+](https://www.python.org/downloads/)
* A working webcam
