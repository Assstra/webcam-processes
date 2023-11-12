import pafy
import cv2


def main():

    # # 1°) Import live from youtube or webcam
    url = "https://www.youtube.com/watch?v=3kPH7kTphnE"
    video = pafy.new(url)
    print(video.title)
    best = video.getbest(preftype="mp4")
    
    # 2°) Show video
    capture = cv2.VideoCapture(best.url)
    while True:
        grabbed, frame = capture.read()
        key = cv2.waitKey(1) & 0xFF
        if frame is None or key == ord("q"):
                # if True break the infinite loop
                break
        # do something with frame here
        image = cv2.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 2)
        cv2.imshow("Output Frame", image)

    # 3°) Process video

main()
