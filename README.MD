# Captcha Solver for Ikabot
Login Captcha Solver for [Ikabot](https://github.com/physics-sp/ikabot)
## Source code
 - The folder `collection` contains all the draggable icons
 - `SolveCaptcha.py` contains a generic function to solve a login captcha
 - `visualizeCaptchaSolver.py` can help you to see the process of detecting icons
 - `testFunctionSolveCaptcha.py` shows you how to use `solveCaptcha()` function
 - `ChopImg.py` contains a function that chops a Captcha image into several pieces
 - `IkabotSimulation.py` is an example of use based on Ikabot
## Getting Started
**You will need to Install Tesseract**

**1**. Install tesseract using windows installer available at:  [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

**2**. Note the tesseract path from the installation. Default installation path at the time of this edit was:  `C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe`. It may change so please check the installation path.

**3**.  `pip install pytesseract`

**4**. Set the tesseract path (`TESSERACT_PATH`) in the script
## Contribution
All images have been listed in the collection at the time of this edit.</br>
If you want to add icons in the collection, you have to add the `.png` file in the folder `collection`.

## Screenshots
**Visualizer :**

![unknown](https://user-images.githubusercontent.com/54487782/234429017-0c38876c-98a2-4217-b19d-66cbf354279a.png)

**Simulation :**

![Screenshot Captcha Solver](https://i.ibb.co/nC5kNWg/2021-07-27-09-07-05-Window.png)

## Acknowledgements
Thanks to [@ikagod](https://github.com/ikagod) for his help and contribution to the repository
