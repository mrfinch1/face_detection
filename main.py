import cv2
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #yüzü algılıyıcak olan sınıflandırıcıyı değişkene atıyoruz

def detect(gray ,frame):
    faces = face_cascade.detectMultiScale(gray,1.3, 5)
    for (x,y ,w ,h) in faces : #face_cascade değişkenini yüzleri bulması için görüntü içinde gezdiriyoruz
        cv2.rectangle(frame , (x,y), (x+w  ,y+h) , (0,255,255) ,2) 
        roi_gray= gray[y:y+h ,x:x+w]                                #çerçeveyi çizme işlemleri
        roi_color= frame[y:y+h ,x:x+w]


        
       
    return frame #bulduğumuz yüzü ekrana basıyoruz
capture = cv2.VideoCapture(0) #Bilgisayarınızda harici kamera varsa 1,2 yapabilirsiniz
while True : #Sürekli görüntü vermesi için sonsuz döngüye alıyoruz
     _, frame =capture.read()  
     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)  
     canvas =detect(gray,frame) 
     cv2.imshow('main',canvas)
     if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 
capture.release() 
cv2.destroyAllWindows() 
