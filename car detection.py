import cv2
box = 0
cap = cv2.VideoCapture('video2.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 10)
    
    box = 0
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),4)
        box = box + 1
        cv2.putText(img, "Car" + str(box), (x,y), cv2.FONT_HERSHEY_SIMPLEX, .6,(255,255,0),3)
    cv2.imshow('video5.mp4', img)

    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
    
 
