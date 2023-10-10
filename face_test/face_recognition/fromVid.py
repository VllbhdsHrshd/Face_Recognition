import face_recognition
import cv2
import os
# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
input_movie = cv2.VideoCapture("/home/jeet/Desktop/Taylor Swift - Style_xvid_002.mp4")
length = int(input_movie.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))

#Now I'm Going to Crete a Directory...
#But First Let me Specify the directory....
directory = "/home/jeet/face_test/face_recognition/Images/"
if not os.path.exists(directory):
 os.mkdir(directory)




# Create an output movie file (make sure resolution/frame rate matches input video!)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
output_movie = cv2.VideoWriter('output.avi', fourcc, 24, (480,320))

# Load some sample pictures and learn how to recognize them.
taylor_image = face_recognition.load_image_file("/home/jeet/Pictures/TAYLOR-SWIFT.jpg")
taylor_face_encoding = face_recognition.face_encodings(taylor_image)[0]

Dominic_image = face_recognition.load_image_file("/home/jeet/Pictures/sherwood1.jpg")
Dominic_face_encoding = face_recognition.face_encodings(Dominic_image)[0]



known_faces = [
    taylor_face_encoding,
Dominic_face_encoding]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "TayLor Swift"
        elif match[1]:
            name = "Dominic Sherwood"

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), -1)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

	# And Writing the images with their names...to a folder using cv2 into a folder named images
	sub_faces = frame[top:bottom,left:right]
	face_name = "/home/jeet/face_test/face_recognition/Images/"+name+".jpg"
	cv2.imwrite(face_name,sub_faces)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)
# All done!
input_movie.release()
cv2.destroyAllWindows()
