import cv2
import time
import numpy as np
import pyautogui
from hand_tracker import HandTracker
from controller_utils import map_coordinates, smooth_movement

# --- CONFIGURATION ---
CAM_WIDTH, CAM_HEIGHT = 640, 480
FRAME_REDUCTION = 100  # Margin around the webcam feed (makes reaching corners easier)
SMOOTHING = 8          # Higher = smoother but more lag (3-7 is good)
CLICK_THRESHOLD = 40   # Distance between fingers to trigger click

# --- SETUP ---
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

tracker = HandTracker(max_hands=1)
screen_w, screen_h = pyautogui.size()

# State variables
ploc_x, ploc_y = 0, 0  # Previous locations
cloc_x, cloc_y = 0, 0  # Current locations

print("Controller Started. Press 'q' to exit.")
print("Gestures:")
print("1. Index Finger UP: Move Cursor")
print("2. Index + Middle UP: Left Click Mode (Pinch to Click)")
print("3. All Fingers UP: Scroll Mode (Move hand up/down)")

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Mirror the image for intuitive movement
    img = cv2.flip(img, 1)
    
    # 1. Find Hand Landmarks
    img = tracker.find_hands(img)
    lm_list = tracker.get_positions(img)

    if len(lm_list) != 0:
        # Get coordinates of Index (8) and Middle (12) finger tips
        x1, y1 = lm_list[8][1:]
        x2, y2 = lm_list[12][1:]

        # Check which fingers are up
        fingers = tracker.get_fingers_up(lm_list)
        # fingers format: [Thumb, Index, Middle, Ring, Pinky]

        # Draw Frame Reduction Box (Area where hand detects movement)
        cv2.rectangle(img, (FRAME_REDUCTION, FRAME_REDUCTION), 
                      (CAM_WIDTH - FRAME_REDUCTION, CAM_HEIGHT - FRAME_REDUCTION),
                      (150, 0, 150), 2)

        # --- MODE 1: MOVING (Only Index Finger Up) ---
        if fingers[1] == 1 and fingers[2] == 0:
            # Convert Coordinates
            x3, y3 = map_coordinates(x1, y1, FRAME_REDUCTION, CAM_WIDTH, CAM_HEIGHT, screen_w, screen_h)
            
            # Smooth Values
            cloc_x, cloc_y = smooth_movement(x3, y3, ploc_x, ploc_y, SMOOTHING)
            
            # Move Mouse
            try:
                pyautogui.moveTo(cloc_x, cloc_y)
            except pyautogui.FailSafeException:
                pass # Ignored for smoother edge experience

            # Update Previous Location
            ploc_x, ploc_y = cloc_x, cloc_y
            
            # Visual Feedback
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

        # --- MODE 2: CLICKING (Index + Middle Fingers Up) ---
        if fingers[1] == 1 and fingers[2] == 1:
            # Find distance between fingers
            length = np.hypot(x2 - x1, y2 - y1)
            
            # Visual marker for clicking mode center
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

            # If distance is short -> CLICK
            if length < CLICK_THRESHOLD:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
                time.sleep(0.1) # Debounce to prevent double clicks

        # --- MODE 3: SCROLLING (All 5 Fingers Up) ---
        # Note: This is a simple implementation. Move hand up to scroll up, down to scroll down.
        if sum(fingers) == 5:
             # Map y position to scroll speed
             if y1 < CAM_HEIGHT // 2 - 50:
                 pyautogui.scroll(30) # Scroll Up
             elif y1 > CAM_HEIGHT // 2 + 50:
                 pyautogui.scroll(-30) # Scroll Down

    # Calculate and Display FPS
    c_time = time.time()
    # (Optional FPS calculation logic here if desired)
    
    cv2.imshow("Gesture Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()