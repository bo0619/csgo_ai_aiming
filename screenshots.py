import cv2
import numpy as np
from mss import mss


screenX = 1920
screenY = 1080

window_size = (
    int(screenX / 2 - 320),
    int(screenY / 2 - 320),
    int(screenX / 2 + 320),
    int(screenY / 2 + 320),
)

screenshot_value = mss()

def screenshot():
    img = screenshot_value.grab(window_size)
    img = np.array(img)
    return img

while True:
    cv2.imshow("test", screenshot())
    cv2.waitKey(1)