from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
options = Options()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options.headless = True
url = "https://translate.google.com/"

def en_to_fren(word):
        browser = webdriver.Firefox(executable_path="/home/david/Desktop/translate/geckodriver", options=options)
        browser.get(url)
        
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable(browser.find_element(By.CLASS_NAME, 'er8xn'))).send_keys(str(word))

        time.sleep(0.3)
        dropdown_button = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]').click()
        french_button = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[35]/div[2]').click()
        while 1 == 1:
            try:
                translation = browser.find_element(By.CLASS_NAME, 'VIiyi')
                if 'Translatio' not in translation.text and translation.text != word:
                    return translation.text
            except:
                pass
        browser.quit()
        