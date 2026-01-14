import numpy as np

def map_coordinates(x, y, frame_r, cam_w, cam_h, screen_w, screen_h):
    """
    Maps webcam coordinates to screen coordinates with a reduction margin (frame_r).
    This allows the user to reach the edges of the screen without stretching their arm too far.
    """
    x_mapped = np.interp(x, (frame_r, cam_w - frame_r), (0, screen_w))
    y_mapped = np.interp(y, (frame_r, cam_h - frame_r), (0, screen_h))
    return x_mapped, y_mapped

def smooth_movement(current_x, current_y, prev_x, prev_y, smoothing_factor):
    """
    Applies simple linear interpolation to reduce jitter.
    """
    # Linear interpolation: Current = Previous + (Target - Previous) / Smoothing
    curr_x = prev_x + (current_x - prev_x) / smoothing_factor
    curr_y = prev_y + (current_y - prev_y) / smoothing_factor
    return curr_x, curr_y