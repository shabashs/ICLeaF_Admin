import configparser
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from Manage_pack.components import components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
config = configparser.RawConfigParser()
config.read('Manage_Pack\my.properties')

class Assign_Pack_To_User:
    def __init__(self, driver):
        self.driver = driver
    def Assign_Pack_To_User(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Pack')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Assign_pack_user')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'Namesearch')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Namesearch')))).send_keys(config.get('ok','nameas'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'search_button')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'usersearch')))).send_keys(
            config.get('ok', 'nameas'))
        components.scroll(self.driver,By.XPATH, config.get('ok', 'editpackdetails'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'editpackdetails')))).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button=WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'serch_again'))))
        ActionChains(self.driver).move_to_element(button).click().perform()
        sub=WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'subject'))))
        ActionChains(self.driver).move_to_element(sub).click().perform()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'selectSubject')))).click()
        Pc=WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'pc_ex'))))
        ActionChains(self.driver).move_to_element(Pc).click().perform()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'add_button')))).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Assign=WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'Assign_button'))))
        ActionChains(self.driver).move_to_element(Assign).click().perform()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'up_pack_msg'))))
        self.driver.save_screenshot(config.get('ok','up_pack_pic'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'okay_button')))).click()

