import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
config = configparser.RawConfigParser()
config.read('Manage_Pack\my.properties')

class Manage_Consent:
    def __init__(self, driver):
        self.driver = driver

    def ManageConsent(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Control')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok','Manage_constent')))).click()
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,config.get('ok','pk_sr')))).send_keys(config.get('ok','content'))
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,config.get('ok','View')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'txtMessage'))))
        self.driver.save_screenshot(config.get('ok', 'Manage_constant_Sc'))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'close')))).click()
        print('Manage Consent automate script run completed')


