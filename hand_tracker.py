# coding utf-8
import cv2
import mediapipe as mp
import time
import sys


mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils


def hand_tracker(img, cv2):
    """

    :param img:
    :param cv2:
    :return:
    """
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_RGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for hand_id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if hand_id == 8 and (cy == 254 or cy > 363):
                    cv2.putText(img, "THAT IS FOREFINGER",
                                (50, 100), cv2.FONT_HERSHEY_PLAIN,
                                3, (255, 0, 255), 3)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


def main_runner():
    """
    main runner
    :return:
    """
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    while True:
        try:
            success, img = cap.read()
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime
            hand_tracker(img, cv2)
            cv2.putText(img, str(int(fps)),
                        (10, 78), cv2.FONT_HERSHEY_PLAIN,
                        3, (255, 0, 255), 3)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        except KeyboardInterrupt:
            print("Interrupted")
            sys.exit(0)


if __name__ == '__main__':
    main_runner()
