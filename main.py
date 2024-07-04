import cv2 
import numpy as np


FPS = 30
TEXT = "АРБУЗЫ"
FONT = cv2.FONT_HERSHEY_COMPLEX
FONT_SCALE = 2
COLOR = (0, 0, 0)
BG_COLOR = 255 # gray bg: rgb = (BG_COLOR, GB_COLOR, BG_COLOR)
TIME = 3
THICKNESS = 4

k = 100
text_width, text_height = cv2.getTextSize(TEXT, FONT, FONT_SCALE, THICKNESS)[0]
step = (text_width + 100) // (TIME * FPS)
y = text_height + ((100 - text_height) // 2) # y-coordinate of text

result = cv2.VideoWriter('result.avi', cv2.VideoWriter_fourcc(*'MJPG'), FPS, (100, 100))

for i in range(FPS * TIME):
	frame = np.full((100, 100, 3), BG_COLOR, dtype=np.uint8)
	cv2.putText(frame, TEXT, (k, y), FONT, FONT_SCALE, COLOR, THICKNESS)
	result.write(frame)
	k -= step

result.release() 
print("Done") 
