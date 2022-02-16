import face_recognition
import cv2

path1 = r"D:\pythonProject2\known\non coded images\Elon_Musk_Royal_Society_(crop1).jpg"
path2 = r"D:\pythonProject2\known\non coded images\download.jpg"

img = cv2.imread(filename=path1)
locations = face_recognition.face_locations(img)
for (a, b, c, d) in locations:
    cv2.rectangle(img, (d, a), (b, c), thickness=2, color=(0, 255, 0))

img2 = cv2.imread(filename=path2)
locations2 = face_recognition.face_locations(img2)
for (a, b, c, d) in locations2:
    cv2.rectangle(img2, (d, a), (b, c), thickness=2, color=(0, 255, 0))

encodings1 = face_recognition.face_encodings(img)  # list
encodings2 = face_recognition.face_encodings(img2)  # list
compare = []
for i in encodings2:
    compare = face_recognition.compare_faces(encodings1, i)
    for j in compare:
        if j:
            print("Matched")
        else:
            print("Not Matched")


cv2.imshow("image1", img)
cv2.imshow("image2", img2)
cv2.waitKey(0)
