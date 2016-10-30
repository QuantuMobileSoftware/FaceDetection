import cv2

key = 0
train = "train.xml"

webcam = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier(train)

while key != 27:
    rval, frame = webcam.read()
    minisize = (frame.shape[1]/2,frame.shape[0]/2)
    miniframe = cv2.resize(frame, minisize)
    faces = classifier.detectMultiScale(miniframe)

    for f in faces:
        x, y, z, t = [ v*2 for v in f ]
        cv2.rectangle(frame, (x,y), (x+z,y+t), (255, 255, 255), 3)

    cv2.imshow("Face Detection", frame)
    key = cv2.waitKey(20)