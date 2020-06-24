from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from locators import *

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator, value)))
        return element

class MainPage(BasePage):
    # method override
    def __init__(self, driver, url):
        # call parent class method
        super(MainPage, self).__init__(driver)
        # navigate to the correct URL
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        field_username = self.wait_for_element(*LoginPageLocators.INPUT_USERNAME)
        field_username.send_keys(username, Keys.RETURN)

        field_password = self.wait_for_element(*LoginPageLocators.INPUT_PASSWORD)
        field_password.send_keys(password, Keys.RETURN)

class DashboardPage(BasePage):
    # method override
    def __init__(self, driver):
        # call parent class method
        super(DashboardPage, self).__init__(driver)

    def get_label_text(self):
        tab_sales = self.wait_for_element(*DashboardPageLocators.SALES_TAB)
        tab_sales.click()
        element = self.wait_for_element(*DashboardPageLocators.LABEL_MSG)
        return element.text
