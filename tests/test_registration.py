import unittest

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from common import config
from pages.registration import RegistrationScreen


class RegistrationTests(unittest.TestCase):
    driver = None
    wait = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(config.APPIUM_SERVER, config.DESIRED_CAPABILITIES)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.reg = RegistrationScreen(cls.wait, cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_001_verify_registration_page_exists(self):
        """
        Verify registration page opens
        """
        self.reg.click_on_next()
        self.assertTrue(self.reg.get_personal_info_field())

