import cv2
import mediapipe as mp
import time
from base import app_runner

cap = cv2.VideoCapture('videos/Le.mp4')
beginTime = 2


@app_runner(beginTime)
def face_run():
    success, img = cap.read()
    print(beginTime)
    pTime = beginTime
    cTime = time.time()
    fps = 1/(cTime - pTime)
    cv2.putText(img, f'FPS: {int(fps)}', (40, 40), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 2)
    cv2.imshow('Image', img)
    cv2.waitKey(20)


if __name__ == '__main__':
    face_run()
