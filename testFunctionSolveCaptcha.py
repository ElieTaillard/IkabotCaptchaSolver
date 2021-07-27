from SolveCaptcha import solveCaptcha
import cv2
from PIL import Image

TEXT_IMAGE_PATH = "img/examples/txt1.png"
CAPTCHA_IMAGE_PATH = "img/examples/img1.png"
COLLECTION_FOLDER_PATH = "img/collection/"

textImg = Image.open(TEXT_IMAGE_PATH)
textImg.load()

captchaImg = cv2.imread(CAPTCHA_IMAGE_PATH)

result = solveCaptcha(textImg, captchaImg, COLLECTION_FOLDER_PATH)

print(result)
