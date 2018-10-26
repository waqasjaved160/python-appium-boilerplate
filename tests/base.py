from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class DriverMethods(object):

    def __init__(self, wait, driver):
        self.wait = wait
        self.driver = driver

    def find_element_by_ios_ui_automation(self, value):
        return self.wait.until(expected_conditions.presence_of_element_located((MobileBy.IOS_UIAUTOMATION, value)))

    def find_elements_by_ios_ui_automation(self, value):
        return self.wait.until(expected_conditions.visibility_of_any_elements_located((MobileBy.IOS_UIAUTOMATION, value)))

    def find_element_by_xpath(self, xpath):
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def find_elements_by_xpath(self, xpath):
        return self.wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath)))

    def find_element_by_class_name(self, class_name):
        return self.wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name)))

    def find_element_by_name(self, name):
        return self.wait.until(expected_conditions.presence_of_element_located((By.NAME, name)))

    def find_elements_by_class_name(self, class_name):
        self.wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name)))
        return self.driver.find_elements_by_class_name(class_name)

    def enter_text(self, selector, text):
        field = self.find_element_by_xpath(selector)
        field.clear()
        field.set_value(text)

    def get_element_by_xpath(self, selector):
        try:
            return self.find_element_by_xpath(selector)
        except TimeoutException:
            return False
