import pytest
from selenium.webdriver.common.by import By

from TestData.config import TestData
from Pages.BasePage import BasePage
from Pages.HR_MGMTPage import HR_MGMTPage
from Pages.Homepage import HomePage


@pytest.mark.usefixtures("init_driver")
class LoginPage(BasePage):
    EMAIL = (By.XPATH, ".//input[@name='username']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ORANGE_HRM_HOME = (By.XPATH, "//a[@href='http://www.orangehrm.com']")

    "constructor of the Login page class"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions'''

    """this is used to get the page title"""

    def get_loginPage_title(self, title):
        return self.get_title(title)

    """this is used to check ORANGE HRM link visibility"""

    def is_orangehrm_link_present(self):
        return self.is_visible(self.ORANGE_HRM_HOME)

    """this is used to check Orange HRM link clickable"""

    def is_orangehrm_link_clickable(self):
        return self.is_clickable(self.ORANGE_HRM_HOME)

    """this is used to click on Orange HRM link"""

    def is_orangehrm_link_click_action_perform(self):
        self.do_click(self.ORANGE_HRM_HOME)
        return HR_MGMTPage(self.driver)

    """this is used to get the page title"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)

    def do_wait(self, waitcount):
        self.driver_imp_wait(waitcount)
