# 'Importing open cv library'

import cv2

# 'Creating objects for cascades'

face_cascade = cv2.CascadeClassifier('C:\\Users\\satya\\Desktop\\Machine Learning\\Haarcascades\\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\satya\\Desktop\\Machine Learning\\Haarcascades\\haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('C:\\Users\\satya\\Desktop\\Machine Learning\\Haarcascades\\haarcascade_smile.xml')

# Capturing face from webcam'

video = cv2.VideoCapture(0)

# 'Creating a program to detect face and smile from webcam'

while True:
    rect, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 3)
    # smile = smile_cascade.detectMultiScale(gray, 1.3, 3)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 225, 0), 3)
        cv2.putText(img, "Face", (420,320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 150), 2)
        cv2.putText(img, "Eyes", (380, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 150), 2, cv2.LINE_AA)
    # for (x, y, w, h) in smile:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (200, 0, 0), 2)
    cv2.imshow('Video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()