import PIL.ImageShow
import cv2
import time
from PIL import ImageGrab, ImageEnhance, ImageOps, Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

img = ImageGrab.grab(bbox=(568, 462, 580, 482))
PIL.ImageShow.show(img)

cores = []
for cor_rgb in img.getdata():
    if cor_rgb not in cores:
        cores.append(cor_rgb)

cores=str(cores)

print(cores)

if cores == "[(255, 255, 255)]":
    print("É branco!")
else:
    print("Não é branco!")
