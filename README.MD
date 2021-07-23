# Captcha Solver
Login Captcha Solver for [Ikabot](https://github.com/physics-sp/ikabot)
## Source code

 - The folder `/collection` contains all the draggable icons
 - Icons are defined in `collection.json`
 - `SolveCaptcha.py` contains a generic function for solving a login captcha
 - `visualizeCaptchaSolver.py` can help you to see the process of detecting icons
 - `testFunctionSolveCaptcha.py` shows you how to use `solveCaptcha()` function
## Getting Started
**You will need to Install Tesseract**

**1**. Install tesseract using windows installer available at:  [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

**2**. Note the tesseract path from the installation. Default installation path at the time of this edit was:  `C:\Users\USER\AppData\Local\Tesseract-OCR`. It may change so please check the installation path.

**3**.  `pip install pytesseract`

**4**. Set the tesseract path (`TESSERACT_PATH`) in the script before calling  `image_to_string`
## Contribution
If you want to add icons in the collection, you have to define the new icon in `collection.json` and add the `.png` file in the folder `/collection`.

## Screenshots
![Screenshot Captcha Solver](https://i.ibb.co/ByT6fp6/Captcha-Solver.png)