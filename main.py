import pafy
import cv2
import numpy as np

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def askUserForVideo():
    print('Enter video url:')
    return input() or "https://www.youtube.com/watch?v=cmkAbDUEoyA"

def main():

    # 1°) Import live from youtube or webcam
    # example_url = "https://www.youtube.com/watch?v=3kPH7kTphnE"
    url = askUserForVideo()
    video = pafy.new(url)
    print(video.title)
    best = video.getbest(preftype="mp4")

    # 2°) Process video

    # 3°) Show video
    capture = cv2.VideoCapture(best.url)
    while True:
        grabbed, frame = capture.read()

        key = cv2.waitKey(1) & 0xFF
        if frame is None or key == ord("q"):
            # if True break the infinite loop
            break

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
            
         # font 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        
        # org 
        org = (50, 50) 
        
        # fontScale 
        fontScale = 1
        
        # Blue color in BGR 
        color = (255, 0, 0) 
        
        # Line thickness of 2 px 
        thickness = 2
        
        print(len(boxes))
        # do something with frame here
        cv2.imshow("Output Frame", frame)


main()
