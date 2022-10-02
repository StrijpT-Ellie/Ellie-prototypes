import cv2
from face_detection import detectFaces;

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detectFaces(frame)

    for i, face in enumerate(faces):
        cv2.rectangle(frame, (int(face[0]), int(face[1])), (int(face[2]), int(face[3])), (255, 0, 0), 2) 

    cv2.imshow("IMG", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()