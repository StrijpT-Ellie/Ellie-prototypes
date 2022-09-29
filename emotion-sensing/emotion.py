### General imports ###
import numpy as np
import cv2
from scipy.ndimage import zoom
import dlib
from keras.models import load_model
from imutils import face_utils

emotions = {
    0: "Angry",
    1: "Disgust",
    2: "Fear",
    3: "Happy",
    4: "Sad",
    5: "Surpised",
    6: "Neutral"
}
global shape_x
global shape_y

def show_webcam() :

    shape_x = 48
    shape_y = 48

    model = load_model('model/emotion-model.h5', compile=False)
    face_detect = dlib.get_frontal_face_detector()
    predictor_landmarks  = dlib.shape_predictor("model/face-landmarks.dat")
    
    #Lancer la capture video
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
                
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = face_detect(gray, 1)

        for (i, rect) in enumerate(rects):

            shape = predictor_landmarks(gray, rect)
            shape = face_utils.shape_to_np(shape)
            
            # Identify face coordinates
            (x, y, w, h) = face_utils.rect_to_bb(rect)
            face = gray[y:y+h,x:x+w]
            
            #Zoom on extracted face
            face = zoom(face, (shape_x / face.shape[0],shape_y / face.shape[1]))
            
            #Cast type float
            face = face.astype(np.float32)
            
            #Scale
            face /= float(face.max())
            face = np.reshape(face.flatten(), (1, 48, 48, 1))
            
            #Make Prediction
            prediction = model.predict(face)
            prediction_result = np.argmax(prediction)
            
            # Rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
            cv2.putText(frame, emotions[prediction_result],(x+w-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

def main():
    show_webcam()

if __name__ == "__main__":
    main()