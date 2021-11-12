import cv2
import time
import hand as htm
import sys




def main_runner():
    """
    main runner
    :return:
    """
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = htm.HandDetector()
    while True:
        try:
            success, img = cap.read()
            # send image into detector
            img = detector.find_hands(img)
            lm_list = detector.find_position(img)
            if len(lm_list) != 0:
                print(lm_list[4])
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


main_runner()