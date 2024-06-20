import configparser
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

config = configparser.RawConfigParser()
config.read('Manage_Pack/my.properties')


class Manage_Corporate_Course:
    def __init__(self, driver):
        self.driver = driver

    def Edit_Course(self):
        wait = WebDriverWait(self.driver, 30)

        # Click on "Manage Corporate Course"
        wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'Manage_corporate_Course')))).click()

        # Click on the next step in "Manage Corporate Course"
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('ok', 'Manage_corporate_co')))).click()
        time.sleep(3)
        # Enter text in search box
        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'usersearch'))))
        search_box.send_keys(config.get('ok', 'test_sub'))
        time.sleep(2)
        # Click the search result
        btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'cursor'))))
        btn1.click()

        # Confirm the action
        element = wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'confi'))))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

        # Add a delay if necessary
        time.sleep(1)

        # Click the plus button
        wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'plus')))).click()

        # Enter the session name
        name = wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'selection_name'))))
        name.send_keys(config.get('ok', 'session'))

        seq = wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'sequence'))))

        time.sleep(3)
        self.driver.execute_script("arguments[0].value = arguments[1];", seq, 2)
        # Save the changes
        wait.until(EC.element_to_be_clickable((By.XPATH, config.get('ok', 'save_button')))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH,config.get('ok','details'))))


        self.driver.save_screenshot("E:/project/Screenshort/config_session.png")
        wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','okay_button'))))
        wait.until(EC.element_to_be_clickable((By.XPATH,config.get('ok','pencile')))).click()


# Ensure the driver is created and passed correctly to the class

