from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")

class DashboardPageLocators(object):
    SALES_TAB = (By.XPATH, "//*[@id='root']/div[1]/div[1]/nav/ul/li[2]/a/div")
    LABEL_MSG = (By.CLASS_NAME, "css-12je7x4-heading-heading--giga")