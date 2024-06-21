import configparser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Manage_pack.components import components
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

config = configparser.RawConfigParser()
config.read('Manage_Pack/my.properties')

class Manage_Corporate_Course:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def Config_Course(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_corporate_Course')))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Manage_corporate_co')))).click()
        time.sleep(3)
        search_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'usersearch'))))
        search_box.send_keys(config.get('ok', 'test_sub'))
        time.sleep(2)
        btn1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'cursor'))))
        btn1.click()
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'confi'))))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        Manage_Corporate_Course.Config_Course_1(self)
        Manage_Corporate_Course.Config_Course_2(self)
        Manage_Corporate_Course.preview(self)
        Manage_Corporate_Course.delete_page(self)

    def Config_Course_1(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'plus')))).click()
        name = self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'selection_name'))))
        name.send_keys(config.get('ok', 'session'))
        seq = self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'sequence'))))
        self.driver.execute_script("arguments[0].value = arguments[1];", seq, 2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'save_button')))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,config.get('ok','details'))))
        self.driver.save_screenshot("E:/project/Screenshort/config_session.png")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','okay_button'))))

    def Config_Course_2(self):
        element_to_hover = self.wait.until(EC.visibility_of_element_located((By.XPATH, config.get('ok', 'mouse'))))
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','New_page')))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','page_Name')))).send_keys("New Page 1")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','sequence_Number'))))#.send_keys(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','choose_file')))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','search_button')))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','Content_Type')))).click()
        components.scroll(self.driver, By.XPATH, config.get('ok', 'save_buttons'))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','save_buttons')))).click()
        components.scroll(self.driver, By.XPATH, config.get('ok', 'add_button'))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','add_button')))).click()
        components.scroll(self.driver, By.XPATH, config.get('ok', 'save_button'))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','reference_link_name')))).send_keys("wikipidia")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','reference_link_Add')))).send_keys(config.get('ok','reference_link'))
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','Yes_radio_button')))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','duration')))).send_keys("30")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','save_button')))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,config.get('ok','details'))))
        self.driver.save_screenshot("E:/project/Screenshort/config_session_1.png")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','okay_button')))).click()

    def preview(self):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','preview_button')))).click()
        new_tab_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab_handle)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','next_button')))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,config.get('ok','close_icon')))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,config.get('ok','close_window'))))
        self.wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','Yes_button')))).click()
        time.sleep(3)
        try:
            self.driver.close() # don't touch this line if u remove the code won't handle the Preview
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            pass

    def delete_page(self):
        element_to_hover = self.wait.until(EC.visibility_of_element_located((By.XPATH, config.get('ok', 'mouse'))))
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'penile')))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'first_delete')))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Yes_button')))).click()