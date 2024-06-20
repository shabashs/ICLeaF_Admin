import configparser
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from Manage_pack.components import components

config = configparser.RawConfigParser()
config.read('Manage_Pack/my.properties')


class CreateUser:
    def __init__(self, driver):
        self.driver = driver

    def create_user(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Pack')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Create_User')))).click()
        name_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_User_Name'))))

        # Generate unique username
        base_name = "User#"
        counter = 1

        while True:
            na = f"{base_name}{counter}"
            print(f"Trying username: {na}")
            name_input.click()
            name_input.clear()
            name_input.clear()
            name_input.send_keys(na)
            name_input.send_keys(Keys.TAB)
            time.sleep(3)

            try:
                warning_element = self.driver.find_element(By.XPATH, config.get('ok', 'exist'))
                if warning_element.is_displayed():
                    print(f"Username {na} is taken, trying next...")
                    counter += 1
                else:
                    break
            except NoSuchElementException:
                break

        print(f"Username {na} is available.")

        # Fill out the rest of the form
        password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_password'))))
        password.send_keys(config.get('ok', 'CUs_Password'))

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_Re_Password')))).send_keys(
            config.get('ok', 'CUs_Password'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_First_Name')))).send_keys(
            config.get('ok', 'First_Name'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_Last_Name')))).send_keys(
            config.get('ok', 'Last_Name'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_mobile')))).send_keys(
            config.get('ok', 'Mobile_No'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_Email')))).send_keys(
            config.get('ok', 'Email'))
        components.scroll(self.driver, By.XPATH, config.get('ok', 'Roll_search'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Roll_search')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Roll_Type_User')))).click()
        components.scroll(self.driver, By.XPATH, config.get('ok', 'CU_check_box'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Roll_is')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Roll_User')))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_check_box')))).click()
        register_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Register_btn'))))
        register_button.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('ok', 'user_created'))))
        self.driver.save_screenshot(config.get('ok', 'screen_shot_for_single'))
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('ok', 'okay_button')))).click()

    def multiple_user(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_Pack')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Create_User')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Multiple_user')))).click()
            time.sleep(3)
            upload = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'upload_User_file'))))
            time.sleep(3)
            upload.send_keys(config.get('ok', 'user_file_path'))

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'parse_button')))).click()
            components.scroll(self.driver, By.XPATH, config.get('ok', 'for_scroll'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Cr_User_search')))).send_keys(
                config.get('ok', 'change'))
            pencil = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'pencil'))))
            ActionChains(self.driver).move_to_element(pencil).click().perform()
            time.sleep(4)
            first_name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'First'))))
            first_name.send_keys(Keys.CONTROL + 'a')
            first_name.send_keys(config.get('ok', 'new_name'))
            last_name = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Last'))))
            last_name.send_keys(Keys.CONTROL + 'a')
            last_name.send_keys(config.get('ok', 'new_last'))
            email = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'chang_Email'))))
            email.send_keys(Keys.CONTROL + 'a')
            email.send_keys(config.get('ok', 'New_mail'))
            password = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'change_password'))))
            password.send_keys(Keys.CONTROL + 'a')
            password.send_keys(config.get('ok', 'New_password'))
            mobile = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Change_mobile'))))
            mobile.send_keys(Keys.CONTROL + 'a')
            mobile.send_keys(config.get('ok', 'New_mobile'))
            components.scroll(self.driver, By.XPATH, config.get('ok', 'click_here'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'click_here')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'close')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'CU_check_box')))).click()
            components.scroll(self.driver, By.XPATH, config.get('ok', 'Multiple_register'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Multiple_register')))).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, config.get('ok', 'message_multipel'))))
            self.driver.save_screenshot(config.get('ok', 'Screen_shot_for_multiple_user'))
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('ok', 'okay_button')))).click()
            print('Create user Pack successfully automated ')

        except Exception as e:
            print("Exception handled on Multiple user create Pack the Undefined error is\n", e)
            pass
