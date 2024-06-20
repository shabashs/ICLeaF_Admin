import configparser
from selenium.webdriver import Keys
from Manage_pack.components import components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
config = configparser.RawConfigParser()
config.read('Manage_Pack\my.properties')

class Update_User:
    def __init__(self, driver):
        self.driver = driver
    def Update_User(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Pack')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Update_user')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'see')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'filterBy')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Cr_User_search')))).send_keys(
                config.get('ok', 'change'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'first_button')))).click()
            components.scroll(self.driver, By.XPATH, config.get('ok', 'rows'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'secon_serch')))).send_keys(
                config.get('ok', 'dt'))
            components.scroll(self.driver, By.XPATH, config.get('ok', 'Cr_User_search'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'first_edit')))).click()
            time.sleep(5)
            password = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_password'))))
            password.send_keys(Keys.CONTROL + 'a')
            password.send_keys(config.get('ok', 'New_password'))
            repassword = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_Re_Password'))))
            repassword.send_keys(Keys.CONTROL + 'a')
            repassword.send_keys(config.get('ok', 'New_password'))
            name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'first_name_ag'))))
            name.send_keys(Keys.CONTROL + 'a')
            name.send_keys(config.get('ok', 'new_name'))
            mobile = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'newMobile'))))
            mobile.send_keys(Keys.CONTROL + 'a')
            mobile.send_keys(config.get('ok', 'New_mobile'))
            components.scroll(self.driver, By.XPATH, config.get('ok', 'Update_button'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Update_button')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ok', 'Update_button'))))
            self.driver.save_screenshot(config.get('ok', 'Screen_shot_for_multiple_user_ag'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'okay_button')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'first_delete')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Yes_button')))).click()
            print('View and Update user Pack successfully automated ')
        except Exception as e:
            print("Exception handled on View and Update user Pack the Undefined error is\n", e)
            pass












