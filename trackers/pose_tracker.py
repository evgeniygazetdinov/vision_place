import cv2
import mediapipe as mp
from base import app_runner


class PoseDetector:
    def __init__(self,
                 mode=False, up_body=False, smooth=True,
                 detector_con=0.5, track_con=0.5):
        self.mode = mode
        self.up_body = up_body
        self.smooth = smooth
        self.detector_con = detector_con
        self.track_con = track_con

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.mode, self.up_body, self.smooth, self.detector_con,
                                      self.track_con)

    def find_pose(self, img, draw=True):
        """

        :param img:
        :param draw:
        :return:
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(img_rgb)
        if results.pose_landmarks:
            if draw:
                self.mp_draw.draw_landmarks(img, results.pose_landmarks,
                                            self.mp_pose.POSE_CONNECTIONS)
        return img

    def find_points(self):


@app_runner
def main(detector):

    success, img = cap.read()
    img = detector.find_pose(img)

    # for dot_id, lm in enumerate(results.pose_landmarks.landmark):
    #     h, w, c = img.shape
    #     cx, cy = int(lm.x * w), int(lm.y * h)
    #     cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    cv2.imshow('Image', img)
    cv2.waitKey(1)


if __name__ == '__main__':
    cap = cv2.VideoCapture('videos/Le.mp4')
    detector = PoseDetector()
    main(detector)