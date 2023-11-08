# TREŚĆ ZADANIA:
# Napisz program, który odczytuje tekst z obrazu
# zawierającego numer tablicy rejestracyjnej samochodu, a
# następnie sprawdza, czy numer jest poprawny i zgodny z
# formatem.
import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gofrf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    # Funkcja do odczytywania tekstu z obrazu
def extract_text_from_image(image_path):
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text

image_path = 'tablica1.jpg'
text = extract_text_from_image(image_path)
# Output to:
# Numer tablicy rejestracyjnej: 4PJ54
# VOLKSWAGEN GROUP POLSKA więc to trzeba wwyciąć

numer = text.split()[0].strip()


#tablica musi miec od 5 do 7 znaków alfanumerycznych
regex = r'^.{1,10}$'
t1 =str(numer)

if bool(re.match(regex, t1)):
    print("Numer tablicy rejestracyjnej:", t1)
    print("Poprawny format")
else:
    print("Numer tablicy rejestracyjnej nie jest zgodny z formatem.")


