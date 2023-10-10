import numpy
import cv2
import dlib
import face_recognition
from PIL import Image
#first testing for face detection ie..  finding facial features

# this statement converts the loaded file into numpy array
image = face_recognition.load_image_file('/home/jeet/Desktop/rs_634x634-160609141448-634-anna-kournikova-enrique-iglesias-060916.jpg')

face_location = face_recognition.face_locations(image)

#finding the number of face in the given pic or file
print("found {} face(s) in this photograph.".format(len(face_location)))

# now we're all set to display them ....
for faces in face_location:
		    top,right,bottom,left = faces
		    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,right))
		    # You can access the actual face itself like this:
   		    face_image = image[top:bottom, left:right]
	   	    pil_image = Image.fromarray(face_image)
                    pil_image.show()		

