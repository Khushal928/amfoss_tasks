                             README.MD                                       
in this task, we have to create an image with an arithemetic expression in it.
Then we have to write a python code which scan the picture and return the
evaluated value of expression in the picture


I have used imagemagick to create .png file, image_to_string in pytesseract
to get string from text


I have used imagemagick to create the image <br>
to download imagemagick, 
```
sudo apt install imagemagick 
convert -background blue -fill red -font Arial -pointsize 30 label:'7+12' captcha.png 
```
and this is the image downloaded<br>
[image](captcha.png)


to scan images, I have used pytesseract. but to install and use this module, we
need to do it in virtual environment. so to install venv to create and use virtual environments,
```
sudo apt install python3.12 -venv
python3 -m venv captcha
source captcha/bin/activate
```
to install pytesseract,
```
pip install pytesseract
```
we even need another tool to manage with .png files. I have used pillow. to install pillow,
```
pip install pillow
```


now that all the tools are installed, here is the code!
```python
import pytesseract
from PIL import Image
imgpointer=Image.open('captchaimg.png')
textinimage=pytesseract.image_to_string
print(textinimage,'=',eval(textinimage))
```


and this is the output<br>
[image](pastedimage.png)