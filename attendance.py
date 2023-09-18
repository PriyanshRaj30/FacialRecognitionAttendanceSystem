import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
print("Success")


video_capture = cv2.VideoCapture(0)

#load images
my_img = face_recognition.load_image_file("faces/myimg.jpg")
my_img_encoding = face_recognition.face_encodings(my_img)[0]

known_face_name = ["priyansh"]
known_face_encoding = [my_img_encoding]

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



    cv2.imshow("Atendence",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
