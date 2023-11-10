# Napisz program, który odczytuje tekst z obrazu
# zawierającego tytuł i fragment artykułu prasowego, a
# następnie podsumowuje treść artykułu i wyświetla źródło i
# datę publikacji


import pytesseract
import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gofrf\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

    # Funkcja do odczytywania tekstu z obrazu
def extract_text_from_image(image_path):
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text

image_path = 'artykul2.PNG'
text = extract_text_from_image(image_path)

first15Words= text.split()[:15]
lacznik= " "
textToBeSearch= lacznik.join((first15Words))
print(textToBeSearch)

driver = webdriver.Firefox()
driver.get("https://www.google.com")
consent = driver.find_element("xpath", ("//*[@id=\"L2AGLb\"]/div"))
consent.click();
print("cookes accepted")
time.sleep(3)
print("now searching bar")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#APjFqb'))
)

#
# box = driver.find_element("xpath", ('/html/body/div[2]/div/div/main/div[1]/div/div[2]/button/input'))
element.send_keys(textToBeSearch)
element.send_keys(Keys.RETURN)
time.sleep(2)
first_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)'))
)
first_link.click()
current_url = driver.current_url
author_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.indicator__authorname'))
)

print("Zrodlo to ", current_url)
print("Autor to ", author_element.text)
driver.close()
