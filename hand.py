# coding utf-8
import cv2
import mediapipe as mp
import time
import sys


class HandDetector:
    def __init__(self, mode=False, max_hands=2, complexity=1,
                 detect_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detect_con = detect_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.complexity,
                                         self.detect_con, self.track_con)
        self.mp_draw = mp.solutions.drawing_utils
        self.results = []

    def find_hands(self, img, draw=True):
        """

        :param img:
        :param draw:
        :return:
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_number=0, draw=True):
        lm_list = []

        for hand_id, lm in enumerate(
                handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy)
            if hand_id == 8 and (cy == 254 or cy > 363):
                cv2.putText(img, "THAT IS FOREFINGER",
                            (50, 100), cv2.FONT_HERSHEY_PLAIN,
                            3, (255, 0, 255), 3)
        return lm_list

def hand_tracker(img, cv2):
    """

    :param img:
    :param cv2:
    :return:
    """




def main_runner():
    """
    main runner
    :return:
    """
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        try:
            success, img = cap.read()
            # send image into detector
            img = detector.find_hands(img)
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime

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
