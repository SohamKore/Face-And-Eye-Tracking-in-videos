# iNstall : pip install opencv-python

import cv2

# Load the pre-trained face detector (you may need to download it)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the pre-trained eye detector (you may need to download it)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the video
video_path = r'eyecontactVideo.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Create an OpenCV window with resizable flag
cv2.namedWindow('Face and Eye Tracking', cv2.WINDOW_NORMAL)

# Initialize the number of people counter
num_people = 0

# Loop through each frame in the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the region of interest (ROI) within the face rectangle
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))

        # Draw rectangles around the detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Calculate the position of the eyes relative to the face ROI
            eye_x = x + ex + ew // 2
            eye_y = y + ey + eh // 2

            # Determine the direction of gaze based on the eye position
            if eye_x < x + w // 3:
                direction = 'Left'
            elif eye_x > x + 2 * w // 3:
                direction = 'Right'
            else:
                direction = 'Straight ahead'

            # Draw a circle at the eye position and print the direction of gaze
            cv2.circle(frame, (eye_x, eye_y), 4, (0, 0, 255), -1)
            cv2.putText(frame, direction, (eye_x - 70, eye_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Increment the number of people counter
        if num_people == 0:
            num_people += 1

    # Display the number of people currently detected in the video
    cv2.putText(frame, 'People: {}'.format(num_people), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, 'Created by: Soham', (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame in the OpenCV window
    cv2.imshow('Face and Eye Tracking', frame)

    # Check for user input to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
