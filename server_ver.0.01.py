

from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades 
                                     + 'haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = video_capture.read()  # read the camera frame
        if not success:
            break
        else:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                                                gray,
                                                scaleFactor=1.3,
                                                minNeighbors=5,
                                                minSize=(100, 100),
                                                flags=cv2.CASCADE_SCALE_IMAGE
                                            )

            for (x, y, w, h) in faces:
            # for each face on the image detected by OpenCV
            # draw a rectangle around the face
                cv2.rectangle(frame, 
                            (x, y), # start_point
                            (x+w, y+h), # end_point
                            (255, 0, 0),  # color in BGR
                            2) # thickness in px
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
