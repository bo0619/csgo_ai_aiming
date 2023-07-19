import math
import threading
from mss import mss
import cv2
import numpy as np
from ultralytics import YOLO
from sendinput import mouse_xy
from pynput.mouse import Button
from pynput.mouse import Listener


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
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img

is_middle_clicked = False

def mouse_click(x, y, button, pressed):
    global is_middle_clicked
    print(x, y, button, pressed)
    if pressed and button == Button.right:
        print("开了！")
        is_middle_clicked = True
    elif not pressed and button == Button.right:
        print("关了！")
        is_middle_clicked = False

def mouse_listener():
    with Listener(on_click=mouse_click) as listener:
        listener.join()
    

model = YOLO("csgo_ai_aiming/csgo_best_v8s.pt")

def run():
    while True:
        img = screenshot()
        results = model(img, conf=0.45, iou=0.6, imgsz=(640, 640))
        results_plotted = results[0].plot()


        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("result", 320, 320)
        cv2.imshow("result", results_plotted)
        cv2.waitKey(1)

        box = results[0].boxes
        distances = []
        # 两层列表，第一层是每个框，第二层是每个框的四个坐标（xywh）
        xywhs = box.xywh.tolist()
        for xywh in xywhs:
            # 相对移动坐标
            move_x = int(xywh[0]) - 320
            move_y = int(xywh[1]) - 320
            distance = math.sqrt(move_x**2 + move_y**2)

            distances.append(distance)
        
        try:
            # 最小距离的索引（敌人位置）
            target_info = xywhs[distances.index(min(distances))]
        except Exception as e:
            pass

        if is_middle_clicked:
            mouse_xy(int(target_info[0] - 320), int(target_info[1] - 320)) # type: ignore

if __name__ == "__main__":  
    threading.Thread(target=mouse_listener).start() # type: ignore   
    run()
