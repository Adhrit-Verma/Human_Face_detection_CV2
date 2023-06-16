import cv2
def facials():
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #path to haarcascade_file
    cam=cv2.VideoCapture(1)
    while True:
        ret, frames=cam.read()
        gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
        status=["Detected","Detecting"]
        object=["Human","Eye"]
            
        faces=face_classifier.detectMultiScale(gray,1.2,7)

        if faces is():
            cv2.putText(frames, status[1], (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,47), 1)

        for (x,y,w,h) in faces:
            rec=cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,43),2)
            cv2.putText(frames, object[0], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,47), 2)
            cv2.putText(frames, status[0], (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,47), 1)


        cv2.imshow("Jimmy's EYE",frames)


# 0xff is the hexadecimal number which helps to check the TRUE value of the given keyword followed by ORD #
# and if the value of the given keyword is TRUE then it will work detecting the keyboard interference #

            
        if (cv2.waitKey(1)==ord("q")):
            cam.release()
            cv2.destroyAllWindows()
            break

        elif (cv2.waitKey(1)==ord("c")):
            cv2.imwrite("E:\JIMMY\Eyes\Captures\capture.jpg",frames)

facials()
