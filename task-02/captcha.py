import pytesseract
from PIL import Image

imgpointer=Image.open('captchaimg.png')
textinimage=pytesseract.image_to_string(imgpointer)
print(textinimage,'=',eval(textinimage))
