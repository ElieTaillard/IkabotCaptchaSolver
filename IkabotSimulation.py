from SolveCaptcha import solveCaptcha, extractText
from ChopImg import chopImg
import cv2
from PIL import Image
import os

COLLECTION_FOLDER_PATH = "img/collection/"


def saveImg(textImg, captchaImg, response):
    name = extractText(textImg)
    # convert from openCV2 to PIL. Notice the COLOR_BGR2RGB which means that
    # the color is converted from BGR to RGB
    color_coverted = cv2.cvtColor(captchaImg, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(color_coverted)

    array = chopImg(pil_image)

    path = os.path.join(COLLECTION_FOLDER_PATH, name + ".png")

    img = array[int(response)-1]
    img.save(path)

    print("Image saved in collection")


def sendToBot(textImg, captchaImg):
    print("Sent to Telegram")
    print("Please enter the number of the correct image (1, 2, 3 or 4)")
    textImg.show()
    cv2.imshow("captcha", captchaImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getUserResponse():
    input1 = input()
    return input1


def main():
    global solvedByTelegram
    print("The interactive captcha has been presented. Trying to solve it...")

    while True:
        TEXT_IMAGE_EXAMPLE_PATH = "img/examples/txt2.png"  # would be an URL in the future
        CAPTCHA_IMAGE_EXAMPLE_PATH = "img/examples/img2.png" # would be an URL in the future

        textImg = Image.open(TEXT_IMAGE_EXAMPLE_PATH)
        textImg.load()

        captchaImg = cv2.imread(CAPTCHA_IMAGE_EXAMPLE_PATH)

        print("Trying to solve the captcha...")
        result = solveCaptcha(textImg, captchaImg, COLLECTION_FOLDER_PATH)
        print(result)

        if result == -1:
            print("Can't solve the captcha. Please solve it via Telegram")
            solvedByTelegram = False
            while True:
                sendToBot(textImg, captchaImg)
                response = getUserResponse()
                if response == '':
                    continue
                solvedByTelegram = True
                break

        captcha_sent = {}
        # captcha_sent = self.s.post('https://image-drop-challenge.gameforge.com/challenge/{}/en-GB'.format(challenge_id), json=data).json()
        captcha_sent['status'] = "solved"
        if captcha_sent['status'] == 'solved':
            captchaSolved = True
            if captchaSolved:
                print("Captcha solved")
                if solvedByTelegram:
                    saveImg(textImg, captchaImg, response)
                break
            else:
                continue


if __name__ == '__main__':
    main()
