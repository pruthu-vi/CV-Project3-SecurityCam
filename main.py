import cv2
import winsound
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame1 = camera.read()
    ret, frame2 = camera.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dialted = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dialted, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 2000: # Detecting larger objects
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        # winsound.Beep(200, 100)
    if cv2.waitKey(10) == ord('q'):     # Press q to turn off the pop-up window
        break
    cv2.imshow('PINKCAM', frame1)   # pop-up camera name is PINKCAM