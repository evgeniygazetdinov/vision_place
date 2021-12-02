import cv2
import mediapipe as mp
import time
from base import app_runner

cap = cv2.VideoCapture('videos/Le.mp4')
beginTime = 0
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

def face_run():
    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)
        if results.detections:
            for id, detection in enumerate(results.detections):
                # print(id, detection.score)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(img, bbox, (255, 0, 255), 2)


        pTime = beginTime
        cTime = time.time()
        fps = 1/(cTime - pTime)
        cv2.putText(img, f'FPS: {int(fps)}', (40, 40), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 2)
        cv2.imshow('Image', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    face_run()
