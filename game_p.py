import cv2
import hand as htm
from base import app_runner

cap = cv2.VideoCapture(0)
detector = htm.HandDetector()


@app_runner
def main_runner():
    """
    main runner
    :return:
    """
    success, img = cap.read()
    # send image into detector
    img = detector.find_hands(img)
    lm_list = detector.find_position(img)
    if len(lm_list) != 0:
        print(lm_list[4])
    cv2.imshow("Image", img)
    cv2.waitKey(1)


if __name__ == '__main__':
    main_runner()