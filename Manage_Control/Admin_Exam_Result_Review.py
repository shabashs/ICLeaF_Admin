import configparser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
config = configparser.RawConfigParser()
config.read('Manage_Pack\my.properties')
class Admin_exam_Review:
    def __init__(self, driver):
        self.driver = driver
    def Select_subject(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Control')))).click()
        timeout = 10
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok','admin_ex_result_review')))).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'deffect'))))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'subject')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Cr_User_search')))).send_keys(
            config.get('ok', 'test'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'pk_sr')))).send_keys(
            config.get('ok', 'pacck'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'secon_serch')))).send_keys(
            config.get('ok', 'ex_name'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Get_sheet')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'admin_result'))))
        self.driver.save_screenshot(config.get('ok', 'Screen_shot_for_Admin_result_screen'))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'close')))).click()
        print('Admin Exam Result\Review automate script run completed')
    def search_by_Subject(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Control')))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'admin_ex_result_review')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'radio_bt_SS')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Box')))).send_keys(config.get('ok','sub1'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'sub_sr')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'pk_sr')))).send_keys(config.get('ok','sub1'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Subjectselect')))).click()
        subject_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'secon_serch'))))
        action = ActionChains(self.driver)
        action.move_to_element(subject_element).perform()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'secon_serch')))).send_keys(config.get('ok','pacck'))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Get_exam')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'thried_search')))).send_keys(config.get('ok','ex_name'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Get_sheet')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'info'))))
        self.driver.save_screenshot(config.get('ok', 'Admin_ex_res_review'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'close')))).click()
        print('Admin_ex_res_review from the Manage Control test script ran successfully !!')