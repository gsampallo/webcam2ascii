import cv2
from os import system
import time
import sys
import array

ASCII_CHARS = [' ','.',':',';','+','*','?','%','S','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]
linea = ''

cap = cv2.VideoCapture(0)
i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aspect_ratio = float(img.shape[0]/img.shape[1])

    new_width = 80
    new_height = int(aspect_ratio * new_width)

    new_dim = (new_width, new_height)  
    buckets = 25  

    image = cv2.resize(img, new_dim, interpolation = cv2.INTER_AREA)

    for x in range (0,new_height):
        for y in range(0,new_width):
            index = int(image[x,y]/buckets)
            linea = linea + ASCII_CHARS[index]
        linea = linea + "\n"

    sys.stdout.write('%s' % linea)
    sys.stdout.flush() 
    time.sleep(0.2)

    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
