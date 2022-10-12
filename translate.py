from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
options = Options()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options.headless = True
from english.french import *
from english.spanish import *



class Translate():
    def __init__(self, geckodriver_path):
        self.url = "https://translate.google.com/"
        self.geckodriver_path = geckodriver_path

    def to_spanish(self, word: str):
        return en_to_span(word=word, geckodriver_path=self.geckodriver_path)
    
    def to_french(self, word: str):
        return en_to_fren(word=word, geckodriver_path=self.geckodriver_path)
# translation = Translate().to_spanish("hello i am stupid")
# print(translation)