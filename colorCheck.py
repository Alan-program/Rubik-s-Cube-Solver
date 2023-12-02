import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('BMin','image',0,255,nothing)
cv2.createTrackbar('GMin','image',0,255,nothing)
cv2.createTrackbar('RMin','image',0,255,nothing)
cv2.createTrackbar('BMax','image',0,255,nothing)
cv2.createTrackbar('GMax','image',0,255,nothing)
cv2.createTrackbar('RMax','image',0,255,nothing)

# Set default value for MAX BGR trackbars.
cv2.setTrackbarPos('BMax', 'image', 255)
cv2.setTrackbarPos('GMax', 'image', 255)
cv2.setTrackbarPos('RMax', 'image', 255)

# Initialize to check if BGR min/max value changes
BMin = GMin = RMin = BMax = GMax = RMax = 0
pBMin = pGMin = pRMin = pBMax = pGMax = pRMax = 0


wait_time = 33

cap=cv2.VideoCapture(0)
while(1):
    ret,image=cap.read()
    image=cv2.flip(image,1)
    output = image
    # get current positions of all trackbars
    BMin = cv2.getTrackbarPos('BMin','image')
    GMin = cv2.getTrackbarPos('GMin','image')
    RMin = cv2.getTrackbarPos('RMin','image')

    BMax = cv2.getTrackbarPos('BMax','image')
    GMax = cv2.getTrackbarPos('GMax','image')
    RMax = cv2.getTrackbarPos('RMax','image')

    # Set minimum and max BGR values to display
    lower = np.array([BMin, GMin, RMin])
    upper = np.array([BMax, GMax, RMax])

    # Create BGR Image and threshold into a range.
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image,image, mask= mask)

    # Print if there is a change in BGR value
    if( (pBMin != BMin) | (pGMin != GMin) | (pRMin != RMin) | (pBMax != BMax) | (pGMax != GMax) | (pRMax != RMax) ):
        print("[%d,%d,%d],[%d,%d,%d]" % (BMin , BMin , GMin, GMax, RMax , RMax))
        pBMin = BMin
        pGMin = GMin
        pRMin = RMin
        pBMax = BMax
        pGMax = GMax
        pRMax = RMax

    # Display output image
    cv2.imshow('image',output)

    # Wait longer to prevent freeze for videos.
    if cv2.waitKey(wait_time) & 0xFF == 27:
        break

cv2.destroyAllWindows()