# Search-Text-in-Images
A python script that performs OCR on the images to search for a specified text. The images will be detected recursively under the given path. The text can be any phrase as well as a regular expression. As a result, the image(s) containing the text will be copied to another directory. It also has some options you can specify according to your needs.

## Requirement:
In the script, [pytesseract](https://pypi.org/project/pytesseract/) which needs Google's Tesseract-OCR to perform optical character recognition (OCR) is used. You can click [here](https://github.com/tesseract-ocr/tessdoc#500x) to download and install Google's Tesseract-OCR.
After that, to install pytesseract:
```
pip3 install pytesseract 
```

## How to run:
First, make sure you specified the options in the script accordingly. After that, to run Search-Text-in-Images:
```
python3 STI.py 
```