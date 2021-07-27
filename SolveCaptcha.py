import pytesseract
import cv2
from PIL import Image
import os

TESSERACT_PATH = "C:/Users/soludev5/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"  # <------ /!\ CHANGE THIS /!\
NUMBER_OF_IMAGE_IN_CAPTCHA = 4

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extractText(textImg):

    new_img = Image.new("RGB", textImg.size, (0, 0, 0))
    new_img.paste(textImg, mask=textImg.split()[3])  # 3 is the alpha channel

    # Perform text extraction
    data = pytesseract.image_to_string(new_img, lang='eng')

    # Format
    data.strip()
    sentence = data[:-3]

    print(sentence)

    # format string
    captchaImgTitle = sentence.split('onto')[0].split('Drag the')[-1].strip()

    return captchaImgTitle


def solveCaptcha(textImg, captchaImg, collectionPath):
    ##############
    # Read Text  #
    ##############

    captchaImgTitle = extractText(textImg)

    # print string
    print(captchaImgTitle)

    ################################
    # Search for img in collection #
    ################################

    imgName = captchaImgTitle.lower().replace(' ', '_') + ".png"
    print(imgName)
    if not os.path.isfile(collectionPath + imgName):
        print("Image not found in collection :(")
        return -1

    print("Image found in collection :D")

    #########################
    # Detect img in Captcha #
    #########################

    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(collectionPath + imgName)
    large_image = captchaImg

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    # Extract the coordinates of our best match
    MPx, MPy = mnLoc

    # Get the size of the template. This is the same size as the match.
    trows, tcols = small_image.shape[:2]

    # Get the coordinates of the template center on large_image
    centerPointx = MPx + int(tcols/2)
    centerPointy = MPy + int(trows/2)

    #################
    # Return number #
    #################

    # Get the width of large_image
    largeWidth = large_image.shape[1]
    # Get the width of 1/N large_image
    widthQuarter = largeWidth/NUMBER_OF_IMAGE_IN_CAPTCHA

    resultReturn = -1

    # Check the location of the centerPointx
    for i in range(0, NUMBER_OF_IMAGE_IN_CAPTCHA):
        if centerPointx >= widthQuarter*i and centerPointx < widthQuarter*(i+1):
            resultReturn = i
            break

    print("img n°", resultReturn+1)

    return resultReturn
