import pytesseract
import cv2
from PIL import Image
import json

def solveCaptcha(textImg, captchaImg):

    TESSERACT_PATH = "C:/Users/soludev5/AppData/Local/Programs/Tesseract-OCR/tesseract.exe" # <------ /!\ CHANGE THIS /!\
    COLLECTION_JSON_PATH = "img/collection.json"
    COLLECTION_FOLDER_PATH = "img/collection/"
    NUMBER_OF_IMAGE_IN_CAPTCHA = 4

    ##############
    # Read Text  #
    ##############

    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    new_img = Image.new("RGB", textImg.size, (0, 0, 0))
    new_img.paste(textImg, mask=textImg.split()[3])  # 3 is the alpha channel

    # Perform text extraction
    data = pytesseract.image_to_string(new_img, lang='eng')

    # Format
    data.strip()
    sentence = data[:-3]

    print(sentence)

    # split string
    spl_string = sentence.split()
    # remove the first 2 words and the last 3 words (remove : "Drag the" and "onto the [...]")
    rm = spl_string[2:-3]
    # convert list to string
    captchaImgTitle = ' '.join([str(elem) for elem in rm])

    # print string
    print(captchaImgTitle)

    ##########################
    # Search for img in json #
    ##########################

    # Open json file
    with open(COLLECTION_JSON_PATH) as jsonFile:
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

    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(COLLECTION_FOLDER_PATH + imgName)
    large_image = captchaImg

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

    #################
    # Return number #
    #################

    # Get the width of large_image
    largeWidth = large_image.shape[1]
    # Get the width of 1/N large_image
    widthQuarter = largeWidth/NUMBER_OF_IMAGE_IN_CAPTCHA

    resultReturn = -1

    # Check the location of the centerPointx
    for i in range(0,NUMBER_OF_IMAGE_IN_CAPTCHA):
        if centerPointx >= widthQuarter*i and centerPointx < widthQuarter*(i+1):
            resultReturn = i
            break

    print("img n°", resultReturn+1)

    return resultReturn
