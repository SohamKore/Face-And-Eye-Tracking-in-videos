# Face-And-Eye-Tracking-in-videos
Enables you to track faces and eyes in a video of people, determines the number of people in the video, and also identifies the direction where each person is looking.

# RUN THE SCRIPT:
Step 1: Install OpenCV

Before running the code, make sure you have OpenCV installed on your system. You can install it by running the following command:
Copy code
pip install opencv-python
Step 2: Download Required XML Files

Download the pre-trained face and eye cascade XML files. You can download them from the following links:
haarcascade_frontalface_default.xml
haarcascade_eye.xml
Save these XML files in the same directory as your Python script.
Step 3: Specify the Video Path

Replace the video_path variable with the path to your video file. Make sure the video file is in a format supported by OpenCV (e.g., .mp4, .avi, etc.).
Step 4: Run the Script

Save the provided code in a Python file with a .py extension (e.g., face_tracking.py).
Open a command prompt or terminal and navigate to the directory where you saved the Python file.
Run the script using the following command:
Copy code
python face_tracking.py
The script will open a window displaying the video with face and eye tracking. The number of people detected in the video will be displayed, along with their eye gaze direction.
Step 5: Exit the Program

To exit the program, press the 'q' key on your keyboard.
Make sure you have OpenCV installed, the required XML files downloaded, and the video file path specified correctly to run the code successfully.
