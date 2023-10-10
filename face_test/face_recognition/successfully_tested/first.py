import numpy 
import face_recognition
import cv2
import dlib
import matplotlib

#loading Taylor's Swift image as an array of Numpy...
taytay = face_recognition.load_image_file("/home/jeet/face_test/known/Taylor-Swift-Promo-Pics-for-her-Album-Reputation-2017.jpg")
unknown = face_recognition.load_image_file("/home/jeet/face_test/unknown/most-popular-music-celeb.jpg")


#getting the encoded image as an array of numpy and further processing..

try:

	taytay_encoding = face_recognition.face_encodings(taytay)[0]
	unknown_encoding = face_recognition.face_encodings(unknown)[1]

except IndexError:
	print("check image file indexes .....Aborting...")
	quit()


known_faces = [taytay_encoding]

#now whatever we've got here is an array of true/false accordingly if the faces matches or not
 	
results = face_recognition.compare_faces(known_faces,unknown_encoding)

print("Is the unknown face a picture of Taylor Swift? {}".format(results[0]))

print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

	
	
