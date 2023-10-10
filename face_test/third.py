import numpy
import cv
import face_recognition
import dlib

#loading the image into numpy array
image = face_recognition.load_image_file("/home/jeet/face_test/unknown/most-popular-music-celeb.jpg")

#finding faces...
face_location = face_recognition.face_locations(image,number_of_times_to_upsample=0, model="cnn")

#sample image and its encoding...
taytay = face_recognition.load_image_file("/home/jeet/face_test/known/Taylor-Swift-Promo-Pics-for-her-Album-Reputation-2017.jpg")
taylor_encoded = face_recognition.face_encodings(taytay)


#no of face(s)
nos = len(face_location)
print(nos)

#declaring the list and later save the encodings from face location into the list
list_of_face_encodings = face_recognition.face_encodings(image)

print(len(list_of_face_encodings))

#print(list_of_face_encodings)


i = 0
k = 0
while (i < nos):

		result=face_recognition.compare_faces(list_of_face_encodings[i],taylor_encoded)
		#print(result)
		if result==[True]:
					print("Taylor can make a bad guy good for a weekend")
					print(i)
					k = i
					break

		i+=1		
	
print(k)
"""
if result[i]==True:
					print("match found")							
		i+=1

"""

		
		
							
	



