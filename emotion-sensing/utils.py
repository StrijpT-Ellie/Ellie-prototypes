import cv2
import dlib
import numpy as np
from imutils.face_utils import FaceAligner


face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("face_detectors/shape_predictor_68_face_landmarks.dat")


def preprocess_img(img, resize):
    if resize:
        img = cv2.resize(img, (48,48), interpolation=cv2.INTER_CUBIC)
    img = img / 255.
    img = np.expand_dims(img, axis = 2)
    img = np.expand_dims(img, axis = 0)
    return img


def bb_to_rect(bb):
    left = bb[0]
    top = bb[1]
    right = bb[2]+bb[0]
    bottom = bb[3]+bb[1]
    return dlib.rectangle(left, top, right, bottom)


def align_face(gray_frame, face, desiredLeftEye):
    face_aligner = FaceAligner(shape_predictor, desiredLeftEye=desiredLeftEye, desiredFaceWidth=48)
    aligned_face = face_aligner.align(gray_frame, gray_frame, face)
    return aligned_face



def draw_text_with_backgroud(img, text, x, y, font_scale, thickness=1, font=cv2.FONT_HERSHEY_SIMPLEX,
                            background=(0,0,0), foreground=(255,255,255), box_coords_1=(-5,5), box_coords_2=(5,-5)):
    (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
    box_coords = ((x+box_coords_1[0], y+box_coords_1[1]), (x + text_width + box_coords_2[0], y - text_height + box_coords_2[1]))
    cv2.rectangle(img, box_coords[0], box_coords[1], background, cv2.FILLED)
    cv2.putText(img, text, (x, y), font, fontScale=font_scale, color=foreground, thickness=thickness)