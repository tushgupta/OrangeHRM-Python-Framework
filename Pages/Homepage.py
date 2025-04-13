import pytest
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


@pytest.mark.usefixtures("init_driver")
class HomePage(BasePage):
    APPLICATION_BTN = (By.XPATH, "//button[@type='button' and text()='Application']")
    SWITCH_SUBSCRIBER_BTN = (By.CSS_SELECTOR, "button.btn.btn-link.text-white.text-decoration-none")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    # LOGOUT_BTN = "Logout"
    USER_DROPDOWN_BTN = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    DASHBOARD_WIDGET = (
    By.XPATH, "//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-dashboard-widget']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_user_dropdown_btn_exist(self):
        return self.is_visible(self.USER_DROPDOWN_BTN)

    def do_user_dropdown_btn_click(self):
        return self.do_click(self.USER_DROPDOWN_BTN)

    def get_user_dropdown_btn_text(self):
        return self.is_visible(self.SWITCH_SUBSCRIBER_BTN)

    # def get_header_value(self):
    #     if self.is_visible(self.HEADER):
    #         return self.get_element_text(self.HEADER)

    def do_logout(self):
        self.navigate_dropdown_items(self.USER_DROPDOWN_BTN)
        self.do_click(self.LOGOUT_BTN)

    def do_wait(self, waitcount):
        self.driver_imp_wait(waitcount)

    def count_widget(self):
        return self.do_count(self.DASHBOARD_WIDGET)
