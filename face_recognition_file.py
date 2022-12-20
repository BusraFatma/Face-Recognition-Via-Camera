import cv2
import face_recognition
import time


isimler = []
tanımlıyüzler = []
print("Opamp Inc.")
time.sleep(1)
print("Yükleniyor...")
time.sleep(3)
print("Örnek dosya Yolu: C:/Users/USER/OneDrive/Masaüstü/Opencv_ile_Python/KLASÖR/RESİM.jpg")
print("Yüz tanımaya geçiş yapmak için 'çıkış' yazın...")
time.sleep(2)

while True:
    a = input("Dosya yolu girin: ")
    if a == "çıkış":
        break
    b = input("Girilen kişinin adı: ")
    
    d = face_recognition.load_image_file(a)
    ayüz1 = face_recognition.face_encodings(d)[0]

    tanımlıyüzler.append(ayüz1)
    isimler.append(b)
    
görüntü = cv2.VideoCapture(0)

list1 = []
list2 = []
list3 = []

while True:
    _, frame = görüntü.read()

    list1 = face_recognition.face_locations(frame)
    list2 = face_recognition.face_encodings(frame,list1)
    print(list1)

    for i in list2:
        eşleşme = face_recognition.compare_faces(tanımlıyüzler, i)
        isim = "Tanımsız"

        if True in eşleşme:
            ilkeşleşme = eşleşme.index(True)
            isim = isimler[ilkeşleşme]
        list3.append(isim)

    for (top, right, bottom, left), name in zip(list1, list2):
     
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 2)      
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, isim, (left + 6, bottom - 6), font, 1.0, (255, 255, 0), 1)
        cv2.putText()

    cv2.imshow("Yuz tanima sistemi", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
görüntü.release()
cv2.destroyAllWindows()
