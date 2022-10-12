import cv2
import time
import numpy as np
from imutils.face_utils import rect_to_bb
from keras.models import load_model
import utils

# Opencv DNN
modelFile = "face_detectors/dnn_tf.pb"
configFile = "face_detectors/dnn_tf.pbtxt"
net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)
conf_threshold = 0.7
emotions = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise'] 

def dnn_detector(frame):
    gray_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    idx = 0

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            idx += 1
            x1 = int(detections[0, 0, i, 3] * frame_width)
            y1 = int(detections[0, 0, i, 4] * frame_height)
            x2 = int(detections[0, 0, i, 5] * frame_width)
            y2 = int(detections[0, 0, i, 6] * frame_height)
            bboxes.append([x1, y1, x2, y2])

            face = [x1, y1, x2-x1, y2-y1]

            img_arr = utils.align_face(gray_frame, utils.bb_to_rect(face), desiredLeftEye)
            img_arr = utils.preprocess_img(img_arr, resize=False)

            predicted_proba = model.predict(img_arr)
            predicted_label = np.argmax(predicted_proba[0])

            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
            text = f"Person {idx}: {emotions[predicted_label]}"
            utils.draw_text_with_backgroud(frame, text, x1 + 5, y1, font_scale=0.4)


desiredLeftEye=(0.32, 0.32)
model = load_model("models/facial_expression.h5")


if __name__ == "__main__":
    iswebcam = True
    vidcap=cv2.VideoCapture(0)

    while True:
        status, frame = vidcap.read()
        if not status:
            break

        if iswebcam:
            frame=cv2.flip(frame,1,0)

            tik = time.time()

            out = dnn_detector(frame)


        cv2.imshow("Face Detection Comparison", frame)
        if cv2.waitKey(10) == ord('q'):
            break

    cv2.destroyAllWindows()
    vidcap.release()
