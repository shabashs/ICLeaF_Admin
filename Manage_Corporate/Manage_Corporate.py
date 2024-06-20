import configparser
from selenium.webdriver import ActionChains
from Manage_pack.components import components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
config = configparser.RawConfigParser()
config.read('Manage_Pack\my.properties')

class create_Corporate:
    def __init__(self, driver):
        self.driver = driver
    def create_New_pack(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_corporate_Course')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Manage_corporate')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ok', 'CreateCorporate')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_name')))).send_keys(
                config.get('ok', 'Name_of_org'))
            mail = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Contact_Email_org'))))
            mail.click()
            mail.clear()
            mail.send_keys(config.get('ok', 'Contact_Email'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'contact_first_name')))).send_keys(
                config.get('ok', 'con_fi_Name'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'contact_last_name')))).send_keys(
                config.get('ok', 'con_Lt_Name'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_add')))).send_keys(
                config.get('ok', 'org_add'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_second_add')))).send_keys(
                config.get('ok', 'org_secod_add'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_City')))).send_keys(
                config.get('ok', 'org_city'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_pin')))).send_keys(
                config.get('ok', 'org_pin'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_user')))).send_keys(
                config.get('ok', 'org_user'))
            password = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_password'))))
            password.click()
            password.clear()
            password.send_keys(config.get('ok', 'org_Password'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Organization_re_password')))).send_keys(
                config.get('ok', 'org_Password'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_mobile')))).send_keys(
                config.get('ok', 'org_mobile'))
            input_field = self.driver.find_element(By.XPATH, config.get('ok', 'organization_Date'))
            input_field.send_keys(config.get('ok', 'org_date'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_check_box')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'save_button')))).click()
            print('create new pack from the Manage corporate test script ran successfully !!')
        except Exception as e:
            print("Exception accord in Manage Corporate Pack \n", e)

    def edit_Corporate(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_corporate_Course')))).click()
            components.get_url(self)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Manage_corporate')))).click()
            serch = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Cr_User_search'))))
            serch.click()
            serch.send_keys(config.get('ok', 'com_name'))
            time.sleep(3)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'edit')))).click()
            components.get_url(self)
            or_name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_name'))))
            self.driver.execute_script("arguments[0].value = '';", or_name)
            or_name.send_keys(config.get('ok', 'Name_of_org'))
            mail = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Email_change'))))
            self.driver.execute_script("arguments[0].value = '';", mail)
            mail.send_keys(config.get('ok', 'Contact_Email'))
            First_name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'contact_first_name'))))
            self.driver.execute_script("arguments[0].value = '';", First_name)
            First_name.send_keys(config.get('ok', 'con_fi_Name'))
            last_name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'contact_last_name'))))
            self.driver.execute_script("arguments[0].value = '';", last_name)
            last_name.send_keys(config.get('ok', 'con_Lt_Name'))
            address = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_add'))))
            self.driver.execute_script("arguments[0].value = '';", address)
            address.send_keys(config.get('ok', 'org_add'))
            other_add = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_second_add'))))
            self.driver.execute_script("arguments[0].value = '';", other_add)
            other_add.send_keys(config.get('ok', 'org_secod_add'))
            city = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_City'))))
            self.driver.execute_script("arguments[0].value = '';", city)
            city.send_keys(config.get('ok', 'org_city'))
            pin = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_pin'))))
            self.driver.execute_script("arguments[0].value = '';", pin)
            pin.send_keys(config.get('ok', 'org_pin'))
            mobile = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'organization_mobile'))))
            self.driver.execute_script("arguments[0].value = '';", mobile)
            mobile.send_keys(config.get('ok', 'org_mobile'))
            input_field = self.driver.find_element(By.XPATH, config.get('ok', 'organization_Date'))
            input_field.send_keys(config.get('ok', 'org_date'))
            components.scroll(self.driver, By.XPATH, config.get('ok', 'save_button'))
            save = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'save_button'))))
            ActionChains(self.driver).move_to_element(save).click().perform()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ok', 'message_fr_C_update'))))
            self.driver.save_screenshot(config.get('ok', 'Edit_corporatr_pic'))
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ok', 'okay')))).click()
            print('create Edit pack from the Manage corporate test script ran successfully !!')
        except Exception as e:
            print("Exception accord in Manage Corporate Pack \n", e)
