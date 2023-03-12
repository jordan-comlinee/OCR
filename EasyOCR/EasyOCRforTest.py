import easyocr
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image
import math
import time

def detectCarNumber(path):
  start = time.time()
  reader = easyocr.Reader(['ko', 'en'])
  result = reader.readtext(path)
  end = time.time()
  print("추론 시간: ", end - start, "초")
  return result


result = detectCarNumber('../testImage/3.jpg')

# 결과 시각화하기
img = cv2.imread('../testImage/3.jpg')
img = Image.fromarray(img)
font = ImageFont.truetype("malgun.ttf", 40)
draw = ImageDraw.Draw(img)

for i in result:
  x = i[0][0][0]
  y = i[0][0][1]
  w = i[0][1][0] - i[0][0][0]
  h = i[0][2][1] - i[0][1][1]

  draw.rectangle(((x, y), (x+w, y+h)), outline="blue", width=2)
  draw.text((int((x+x+w)/2), y-40), str(i[1]), font=font, fill="blue")
plt.imshow(img)
plt.show()
print(result)