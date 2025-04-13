import pytest
from TestData.config import TestData
from Pages.Homepage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Logs.Logs_Create import GetLogs


@pytest.mark.usefixtures("init_driver")
class Test_Home_Page(BaseTest, GetLogs):

    def test_home_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        self.HomePage = HomePage(self.driver)
        home_page = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == self.driver.title

    # '''def test_home_page_dashboard(self):
    #     self.LoginPage = LoginPage(self.driver)
    #     home_page = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     try:
    #         self.LoginPage.set_page_load_timeout(10)
    #         header = home_page.get_header_value()
    #         print(header)
    #         assert header == TestData.HOME_PAGE_HEADER_NAME
    #         HomePage.screenshot_capture(file_name=TestData.FILE_NAME)
    #     except:
    #         self.HomePage.screenshot_capture(TestData.FILE_NAME)
    #         pass'''

    def test_is_application_btn_clickable(self):
        self.HomePage = HomePage(self.driver)
        flag = self.HomePage.is_user_dropdown_btn_exist()
        assert flag

    def test_dashboard_widget_count(self):
        self.HomePage = HomePage(self.driver)
        widget_count = self.HomePage.count_widget()
        assert widget_count == 6

    def test_logout_feature(self):
        self.LoginPage = LoginPage(self.driver)
        self.HomePage = HomePage(self.driver)
        home_page = self.LoginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.HomePage.do_logout()

