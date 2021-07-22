import pytesseract
import cv2
from PIL import Image
import json
import numpy as np
import skimage.exposure

##############
# Read Text  #
##############

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/soludev5/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

png = Image.open('img/examples/txt2.png')
png.load()  # required for png.split()

new_img = Image.new("RGB", png.size, (0, 0, 0))
new_img.paste(png, mask=png.split()[3])  # 3 is the alpha channel

# Perform text extraction
data = pytesseract.image_to_string(new_img, lang='eng')

data.strip()
sentence = data[:-3]

print(sentence)

# split string
spl_string = sentence.split()
# remove the first 2 words and the last 3 words
rm = spl_string[2:-3]
# convert list to string
captchaImgTitle = ' '.join([str(elem) for elem in rm])

# print string
print(captchaImgTitle)


#########################
# Search for img in json#
#########################

# Open json file
with open("img/collection.json") as jsonFile:
    jsonData = json.load(jsonFile)
    jsonFile.close()

imgName = None

# for each img in the json
for imgValue in jsonData:
    if imgValue["title"] == captchaImgTitle:
        imgName = imgValue["name"]
        break

print(imgName)

#########################
# Detect img in Captcha #
#########################


img_rgb = cv2.imread('img/examples/img2.png')
template = cv2.imread('img/collection/' + imgName)
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('Captcha', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
