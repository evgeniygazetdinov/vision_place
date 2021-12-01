from flask import Flask, render_template_string


app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<video id="video" width="640" height="480" autoplay style="background-color: grey"></video>
<button id="snap">Take Photo</button>
<canvas id="canvas" width="640" height="480" style="background-color: grey"></canvas>

<script>

// Elements for taking the snapshot
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream; // assing stream to <video>
        video.play();             // play stream
    });
}

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
    context.drawImage(video, 0, 0, 640, 480);  // copy video frame to canvas
});

</script>
''')

    
if __name__ == '__main__':    
    app.run(debug=True)


from flask import Flask, render_template_string, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''
<video id="video" width="640" height="480" autoplay style="background-color: grey"></video>
<button id="send">Take & Send Photo</button>
<canvas id="canvas" width="640" height="480" style="background-color: grey"></canvas>

<script>

// Elements for taking the snapshot
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// Trigger photo take
document.getElementById("send").addEventListener("click", function() {
    context.drawImage(video, 0, 0, 640, 480); // copy frame from <video>
    canvas.toBlob(upload, "image/jpeg");  // convert to file and execute function `upload`
});

function upload(file) {
    // create form and append file
    var formdata =  new FormData();
    formdata.append("snap", file);
    
    // create AJAX requests POST with file
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{{ url_for('upload') }}", true);
    xhr.onload = function() {
        if(this.status = 200) {
            console.log(this.response);
        } else {
            console.error(xhr);
        }
        alert(this.response);
    };
    xhr.send(formdata);
}

</script>
''')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #fs = request.files['snap'] # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        if fs:
            print('FileStorage:', fs)
            print('filename:', fs.filename)
            fs.save('image.jpg')
            return 'Got Snap!'
        else:
            return 'You forgot Snap!'
    
    return 'Hello World!'
    
    
if __name__ == '__main__':    
    app.run(debug=True, port=5000)

from flask import Flask, render_template_string, request, make_response
import cv2
import numpy as np
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('''

''')

def send_file_data(data, mimetype='image/jpeg', filename='output.jpg'):
    # https://stackoverflow.com/questions/11017466/flask-to-return-image-stored-in-database/11017839
    
    response = make_response(data)
    response.headers.set('Content-Type', mimetype)
    response.headers.set('Content-Disposition', 'attachment', filename=filename)
    
    return response
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #fs = request.files['snap'] # it raise error when there is no `snap` in form
        fs = request.files.get('snap')
        if fs:
            #print('FileStorage:', fs)
            #print('filename:', fs.filename)
            
            # https://stackoverflow.com/questions/27517688/can-an-uploaded-image-be-loaded-directly-by-cv2
            # https://stackoverflow.com/a/11017839/1832058
            img = cv2.imdecode(np.frombuffer(fs.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            #print('Shape:', img.shape)
            # rectangle(image, start_point, end_point, color, thickness)
            img = cv2.rectangle(img, (20, 20), (300, 220), (0, 0, 255), 2)
            
            text = datetime.datetime.now().strftime('%Y.%m.%d %H.%M.%S.%f')
            img = cv2.putText(img, text, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
            #cv2.imshow('image', img)
            #cv2.waitKey(1)
            
            # https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
            ret, buf = cv2.imencode('.jpg', img)
            
            #return f'Got Snap! {img.shape}'
            return send_file_data(buf.tobytes())
        else:
            return 'You forgot Snap!'
    
    return 'Hello World!'
    
    
if __name__ == '__main__':    
    app.run(debug=True, port=5000)


# TODO replace this stuff to golang