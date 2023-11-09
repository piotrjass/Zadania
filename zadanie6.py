# Napisz program, który odczytuje tekst z obrazu
# zawierającego tytuł i fragment artykułu prasowego, a
# następnie podsumowuje treść artykułu i wyświetla źródło i
# datę publikacji


import pytesseract
import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gofrf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    # Funkcja do odczytywania tekstu z obrazu
def extract_text_from_image(image_path):
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text

image_path = 'artykul.PNG'
text = extract_text_from_image(image_path)
# Output to:
# Numer tablicy rejestracyjnej: 4PJ54
# VOLKSWAGEN GROUP POLSKA więc to trzeba wwyciąć
first15Words= text.split()[:15]
lacznik= " "
textToBeSearch= lacznik.join((first15Words))
print(textToBeSearch)

driver = webdriver.Chrome()
