import pytesseract
import cv2
from PIL import Image
import os
import logging

if os.name == 'nt':
  TESSERACT_PATH = "C:/Users/soludev5/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"  # <------ /!\ CHANGE THIS /!\
  pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

NUMBER_OF_IMAGE_IN_CAPTCHA = 4

def extractText(textImg):
    """This function returns a string which represents the name of the image that the text in `textImg` is describing.
    Parameters
    ----------
    textImg : PIL.Image
        a picture that contains text, which can be OCR-ed by tesseract.
        
    Returns
    -------
    captchaImgTitle : str
        a string representing the name of the image that `textImg` is describing.
    """

    new_img = Image.new("RGB", textImg.size, (0, 0, 0))
    new_img.paste(textImg, mask=textImg.split()[3])  # 3 is the alpha channel

    # Perform text extraction
    data = pytesseract.image_to_string(new_img, lang='eng')

    # Format
    data.strip()
    sentence = data[:-3]

    logging.info(sentence)

    # format string
    captchaImgTitle = sentence.split('onto')[0].split('Drag the')[-1].strip()

    return captchaImgTitle


def solveCaptcha(textImg, captchaImg, collectionPath):
    """This function return an integer in the range [0,3]. This integer represents the ordinal position of the image described textually in `textImg`, found in `collectionPath` within `captchaImg`.
    Parameters
    ----------
    textImg : PIL.Image
        a picture that contains text, which can be OCR-ed by tesseract.
    captchaImg : numpy.ndarray
        a picture that contains within itself 4 pictures. This function will search for the index of the image described in `textImg` within this image and return it.
        
    Returns
    -------
    resultReturn : int
        an integer representing the index of the image described in `textImg` within `captchaImg`.
    """
    ##############
    # Read Text  #
    ##############

    captchaImgTitle = extractText(textImg)

    # print string
    logging.info(captchaImgTitle)

    ################################
    # Search for img in collection #
    ################################

    imgName = captchaImgTitle.lower().replace(' ', '_') + ".png"
    assert os.path.isfile(collectionPath + imgName), "Image not found"

    logging.info("Image found in collection :D")

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

    # Check the location of the centerPointx
    for i in range(0, NUMBER_OF_IMAGE_IN_CAPTCHA):
        if centerPointx >= widthQuarter*i and centerPointx < widthQuarter*(i+1):
            resultReturn = i
            break

    logging.info("img n°", resultReturn+1)

    return resultReturn
