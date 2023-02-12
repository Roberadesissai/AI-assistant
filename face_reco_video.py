from fileinput import filename
from operator import index
import cv2
import json
from simple_facerec import SimpleFacerec

face=[]


sfr = SimpleFacerec()
sfr.load_encoding_images("images/")


cap = cv2.VideoCapture(0)

ret, frame = cap.read()
while (ret):
    ret, frame = cap.read()

    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10),cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 3)
        if name:
            face.append(name)

    cv2.imshow("Frame", frame)
    if "Robera" in face:
            break

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
if "Robera" in face:
    names=face.index("Robera")
    name=face[names]
    







cap.release()
cv2.destroyAllWindows()


 
