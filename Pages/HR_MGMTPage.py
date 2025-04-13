import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages.BasePage import BasePage


@pytest.mark.usefixtures("init_driver")
class HR_MGMTPage(BasePage):
    # HEADER = (By.CSS_SELECTOR, "#main-content>div:nth-child(2)>nav>ol>li>p")
    # APPLICATION_BTN = (By.XPATH, "//button[@type='button' and text()='Application']")
    # SWITCH_SUBSCRIBER_BTN = (By.CSS_SELECTOR, "button.btn.btn-link.text-white.text-decoration-none")
    # LOGOUT_BTN = (By.XPATH, "//*[@id='root']/div/div/div/div/header/div/div[4]/button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_HR_MGMT_page_title(self):
        # page_title = self.driver.title
        # self.LoginPage.driver_window_handle(window_id=1)
        # return page_title.getText()
        if len(self.driver.window_handles) > 1:
            self.driver_window_handle(1)
        return self.driver.title
