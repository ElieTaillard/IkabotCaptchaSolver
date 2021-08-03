import cv2
from PIL import Image
import sys
import os
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
from SolveCaptcha import solveCaptcha

TEXT_IMAGE_PATH = "tests/examples/txt1.png"
CAPTCHA_IMAGE_PATH = "tests/examples/img1.png"
COLLECTION_FOLDER_PATH = "collection/"

textImg = Image.open(TEXT_IMAGE_PATH)
textImg.load()

captchaImg = cv2.imread(CAPTCHA_IMAGE_PATH)

result = solveCaptcha(textImg, captchaImg, COLLECTION_FOLDER_PATH)

print(result)
