import cv2
import gtk 
'''
image reading
img = cv2.imread("img/20201019_160153.jpg")
cv2.imshow('Output',img)
cv2.waitKey(0)
'''
cap = cv2.VideoCapture('[DameDesuYo] Shingeki no Kyojin (The Final Season) - 65v0 (1920x1080 10bit AAC) [1031651E].mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if 0xFF == ord('q'):
        break
