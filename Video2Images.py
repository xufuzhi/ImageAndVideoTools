import cv2 as cv
import os

videoPath = './videos/schoolgirls_orig.mp4'
images_result = './imgResults'
imageFormat = '.jpg'

vidcap = cv.VideoCapture(videoPath)
success, image = vidcap.read()
count = 0
while success:
    cv.imwrite(os.path.join(images_result, str(count).zfill(5) + imageFormat), image)
    success, image = vidcap.read()
    count += 1

print('end!')
