import pytesseract
import cv2
from PIL import Image
import os

TESSERACT_PATH = "C:/Users/soludev5/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
COLLECTION_FOLDER_PATH = "collection/"

TEXT_IMAGE_PATH = "tests/examples/txt2.png"
CAPTCHA_IMAGE_PATH = "tests/examples/img2.png"

##############
# Read Text  #
##############

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

png = Image.open(TEXT_IMAGE_PATH)
png.load()  # required for png.split()

new_img = Image.new("RGB", png.size, (0, 0, 0))
new_img.paste(png, mask=png.split()[3])  # 3 is the alpha channel

# Perform text extraction
data = pytesseract.image_to_string(new_img, lang='eng')

# Format
data.strip()
sentence = data[:-3]

print(sentence)

# format string
captchaImgTitle = sentence.split('onto')[0].split('Drag the')[-1].strip()

# print string
print(captchaImgTitle)


################################
# Search for img in collection #
################################

imgName = captchaImgTitle.lower().replace(' ','_') + ".png"
assert os.path.isfile(COLLECTION_FOLDER_PATH + imgName), "Image not found in collection"


print(imgName)

#########################
# Detect img in Captcha #
#########################

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread(COLLECTION_FOLDER_PATH + imgName)
large_image = cv2.imread(CAPTCHA_IMAGE_PATH)

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn, _, mnLoc, _ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx, MPy = mnLoc

# Get the size of the template. This is the same size as the match.
trows, tcols = small_image.shape[:2]

# Get the coordinates of the template center on large_image
centerPointx = MPx + int(tcols/2)
centerPointy = MPy + int(trows/2)

# Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx, MPy),
              (MPx+tcols, MPy+trows), (0, 255, 255), 2)
cv2.circle(large_image, (centerPointx, centerPointy),
           radius=2, color=(0, 255, 255), thickness=-1)

# Display the original image with the drawing
cv2.imshow('output', large_image)


#################
# Return number #
#################

# Get the width of large_image
largeWidth = large_image.shape[1]
# Get the width of 1/4 large_image
widthQuarter = largeWidth/4

resultReturn = -1

# Check the location of the centerPointx
if centerPointx >= 0 and centerPointx < widthQuarter:
    resultReturn = 0
elif centerPointx >= widthQuarter and centerPointx < widthQuarter*2:
    resultReturn = 1
elif centerPointx >= widthQuarter*2 and centerPointx < widthQuarter*3:
    resultReturn = 2
elif centerPointx >= widthQuarter*3 and centerPointx < widthQuarter*4:
    resultReturn = 3

print("img n°", resultReturn+1, ": return", resultReturn)

# The image is only displayed if we call this
cv2.waitKey(0)
cv2.destroyAllWindows()
