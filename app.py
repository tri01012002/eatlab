from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
import os
import cv2

app = Flask(__name__)

model = YOLO('D:\ProjectAI\eatlab\models\\bestmodel\weights\\best.pt')

UPLOAD_FOLDER = 'upload'
OUTPUT_FOLDER = 'output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)

    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = cv2.imread(filename)
        results = model.predict(img, conf=0.5)
        output_image_path = os.path.join(app.config['OUTPUT_FOLDER'], 'output_image.jpg')
        for result in results[0].boxes:
            x1, y1, x2, y2 = result.xywh[0]
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(img, f'{result.cls.item()} {result.conf.item():.2f}',
                        (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imwrite(output_image_path, img)
        return jsonify({'message': 'images were processed and stored', 'output_file': output_image_path})

    else:
        video_path = filename
        cap = cv2.VideoCapture(video_path)
        frames_results = []

        output_video_path = os.path.join(app.config['OUTPUT_FOLDER'], 'output_video.mp4')
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (640, 480))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model.predict(frame, conf=0.5)
            for result in results[0].boxes:
                x1, y1, x2, y2 = result.xywh[0]
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f'{result.cls.item()} {result.conf.item():.2f}',
                            (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            out.write(frame)

        cap.release()
        out.release()

        return jsonify({'message': 'Video was processed and stored', 'output_file': output_video_path})


if __name__ == '__main__':
    app.run(debug=True)
