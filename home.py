import cv2, time
from datetime import datetime
import argparse
import os

# Load Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start webcam
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
        for x, y, w, h in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            exact_time = datetime.now().strftime("%Y-%b-%d-%H-%M-%S-%f")
            cv2.imwrite("face detected" + str(exact_time) + ".jpg", img)

    cv2.imshow("home surv", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        # Handle command line arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-ext", "--extension", required=False, default='jpg')
        ap.add_argument("-o", "--output", required=False, default='output.mp4')
        args = vars(ap.parse_args())

        dir_path = '.'
        ext = args['extension']
        output = args['output']

        break

video.release()
cv2.destroyAllWindows()

# ---------------- Convert Captured Images into Video ----------------

images = []

# Collect all images with given extension
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Read first image to get size
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
height, width, channels = frame.shape

# Define video codec and create VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 5.0, (width, height))

# Write all frames into video
for image in images:
    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)
    out.write(frame)

out.release()
cv2.destroyAllWindows()


#Finally Pressed Q button to stop