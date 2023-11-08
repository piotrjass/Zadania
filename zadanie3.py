# Napisz program, który odczytuje tekst z obrazu
# zawierającego nazwę kraju i flagę, a następnie wyświetla
# informacje o tym kraju, takie jak stolica, waluta, populacja
# itp.

import pytesseract
import cv2
from countryinfo import CountryInfo
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gofrf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image_path):
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text

image_path = 'flag.png'
text = extract_text_from_image(image_path)
name= str(text).rstrip('\n')

print(name)
country = CountryInfo(name)
data2 = country.capital()
print(data2)
data3 = country.currencies()
print(data3)
data4 = country.languages()
print(data4)
data5 = country.timezones()
print(data5)
data6 = country.area()
print(data6)
data7 = country.borders()
print(data7)
data8 = country.calling_codes()
print(data8)
