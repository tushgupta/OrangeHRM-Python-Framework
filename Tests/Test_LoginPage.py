import pytest

from TestData.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.Homepage import HomePage
from Pages.HR_MGMTPage import HR_MGMTPage
from Logs.Logs_Create import GetLogs


@pytest.mark.usefixtures("init_driver")
class Test_Login(BaseTest, GetLogs):

    def test_orangehrm_page_visible(self):
        self.LoginPage = LoginPage(self.driver)
        flag = self.LoginPage.is_orangehrm_link_present()
        assert flag

    def test_orangehrm_page_clickable(self):
        self.LoginPage = LoginPage(self.driver)
        flag = self.LoginPage.is_orangehrm_link_clickable()
        assert flag
        self.LoginPage.driver_window_handle(0)

    def test_orangehrm_page_click_action(self):
        self.LoginPage = LoginPage(self.driver)
        self.HR_MGMTPage = HR_MGMTPage(self.driver)
        self.LoginPage.is_orangehrm_link_click_action_perform()
        # self.LoginPage.driver_window_handle(window_id=1)
        title = self.HR_MGMTPage.get_HR_MGMT_page_title()
        print(title)
        assert title == TestData.HR_MANAGEMENT_PAGE_TITLE

    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == self.driver.title

    def test_login(self):
        log = self.get_loggers()
        self.LoginPage = LoginPage(self.driver)
        self.HomePage = HomePage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = self.HomePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        # assert title == "abc"
        assert title == self.driver.title
