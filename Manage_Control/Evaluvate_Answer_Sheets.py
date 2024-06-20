import configparser
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from Manage_pack.components import components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
config = configparser.RawConfigParser()
config.read('Manage_Pack\my.properties')

class Evaluate_answer_sheet:
    def __init__(self, driver):
        self.driver = driver

    def EValuate_sheet(self):
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Control')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,config.get('ok','Evaluate')))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'see')))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'subject')))).click()
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,config.get('ok','Cr_User_search')))).send_keys(config.get('ok','test'))
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,config.get('ok','Answer_sheet')))).click()
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,config.get('ok','ss'))))
        self.driver.save_screenshot(config.get('ok', 'Admin_result_screen'))
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,config.get('ok','close')))).click()
        print('Evaluate Answer Sheet automate script run completed')












