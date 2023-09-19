import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
print("Success")


video_capture = cv2.VideoCapture(0)

#load images
Rock = face_recognition.load_image_file("faces/rock.jpg")
Rock_encoding = face_recognition.face_encodings(Rock)[0]

Priyansh = face_recognition.load_image_file("faces/myimg.jpg")
Priyansh_encoding = face_recognition.face_encodings(Priyansh)[0]

known_face_name = ["Rock","Priyansh"]
known_face_encoding = [Rock_encoding, Priyansh_encoding]

# - list of expected faces
student = known_face_name.copy()
face_locations = []
face_encodings = []
while True:
    success, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Recognize faces
    face_locations = face_recognition.face_locations (rgb_small_frame)
    face_encodings = face_recognition.face_encodings (rgb_small_frame, face_locations)
    #Compare it with saved faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
        best_match = np.argmin(face_distance)

        if(matches[best_match]):
            name = known_face_name[best_match]

            if name in known_face_name:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale = 1
                fontColor = (186, 205, 15)
                thickness = 2 
                lineType = 1
                cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
            

    cv2.imshow("Atendence",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

