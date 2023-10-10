import numpy
import cv2
import dlib
import face_recognition
from PIL import Image
#first testing for face detection ie..  finding facial features

# this statement converts the loaded file into numpy array
image = face_recognition.load_image_file("/home/jeet/face_test/unknown/most-popular-music-celeb.jpg")

face_location = face_recognition.face_locations(image,number_of_times_to_upsample=0, model="cnn")

#finding the number of face in the given pic or file
print("found {} face(s) in this photograph.".format(len(face_location)))

# now we're all set to display them ....
i=0
for faces in face_location:

		    if i==4:

			    top,right,bottom,left = faces
			    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,right))
			    # You can access the actual face itself like this:
	   		    face_image = image[top:bottom, left:right]
		   	    pil_image = Image.fromarray(face_image)
			    print(type(pil_image))
		            pil_image.show()	
	
		    i+=1
