from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


"""This class is the parent of all pages"""
"""IT contains all generic methods and Page for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def screenshot_capture(self, file_name):
        return self.driver.get_screenshot_as_file("/Users/tushargupta/Docuverus/Test_Reports/ {}".format(file_name))

    def driver_imp_wait(self, impwait):
        return self.driver.implicitly_wait(impwait)

    def driver_window_handle(self, window_id):
        # Open a new window
        # self.driver.execute_script("window.open('');")
        # # Switch to the new window and open URL B
        # self.driver.get("https://www.orangehrm.com/")
        # Switch back to the first tab with URL A

        # Get the current window handle
        # current_window = self.driver.current_window_handle

        # Get all window handles
        window_handles = self.driver.window_handles
        return self.driver.switch_to.window(window_handles[window_id])

        #
        # # Switch to a new window (assuming more than one window is open)
        # for handle in window_handles:
        #     if handle != current_window:
        #         self.driver.switch_to.window(handle)
        #         break

    def navigate_dropdown_items(self, by_drp_options):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_drp_options)).click()

    def do_count(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for i in elements:
            elem_count = (len(elements))
            return elem_count
