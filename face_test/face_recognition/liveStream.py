import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference from WebCam
video_capture =  cv2.VideoCapture(0)


# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
'''
fourcc = cv2.cv.CV_FOURCC(*'XVID')
output_movie = cv2.VideoWriter('output.avi', fourcc, 24, (480,320))
'''

# Load some sample pictures and learn how to recognize them.
taylor_image = face_recognition.load_image_file("/home/jeet/Pictures/TAYLOR-SWIFT.jpg")
taylor_face_encoding = face_recognition.face_encodings(taylor_image)[0]

Dominic_image = face_recognition.load_image_file("/home/jeet/Pictures/sherwood1.jpg")
Dominic_face_encoding = face_recognition.face_encodings(Dominic_image)[0]



known_faces = [
    taylor_face_encoding,
Dominic_face_encoding]

known_faces_name = ["Taylor","Dom"]


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
#frame_number = 0
process_this_frame = True


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #Resizing the frame size to its one-fourth of its image
    small_frame = cv2.resize(frame,(0,0),fx = 0.25,fy = 0.25)

"""
    # Quit when the input video file ends
    if not ret:
        break
"""

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
		# Find all the faces and face encodings in the current frame of video
		    face_locations = face_recognition.face_locations(rgb_small_frame)
		    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)    
		
		    face_names = []
		    for face_encoding in face_encodings:
       			 # See if the face is a match for the known face(s)
		         matches = face_recognition.compare_faces(known_faces, face_encoding)

		        
		         name = "Unknown"
		        
			 if True in matches:
						first_match_index = matches.index(True)
						name = known_faces_name[first_match_index]


 		         face_names.append(name)

    process_this_frame = not process_this_frame
	
    #displaying the result
      for (top, right, bottom, left), name in zip(face_locations, face_names):
        #if not name:
         #   continue
	top*=4
	right*=4
	bottom*=4
	left*=4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), -1)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

	# And Writing the images with their names...to a folder using cv2 into a folder named images
	sub_faces = frame[top:bottom,left:right]
	face_name = "/home/jeet/face_test/face_recognition/newLive/"+name+".jpg"
	cv2.imwrite(face_name,sub_faces)

	
    #Displaying the resulting image

 cv2.imshow('Video', frame)
 if cv2.waitKey(1) & 0xFF == ord('q'):
					break


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
