import os
from datetime import datetime

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from TestData.config import TestData


# params=["Chrome", "Firefox"],


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )


@pytest.fixture(scope='class')
def init_driver(request):
    # global driver
    browser_name = request.config.getoption("--browser_name").lower()

    if browser_name == "chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('--disable-cache')
        # chrome_option.add_argument('--headless=new')
        chrome_option.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid browser parameter: {browser_name}")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def _capture_screenshot(driver, name):
    # driver.get_screenshot_as_file(name)

    # Define your custom path
    folder_path = "/Users/tushargupta/Docuverus/Screenshots"

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Full path where the screenshot will be saved
    full_path = os.path.join(folder_path, name)

    # Save the screenshot
    driver.save_screenshot(full_path)
    return full_path  # return it if you want to use it in HTML embedding

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # if report.when == 'call' or report.when == "setup":
    #     xfail = hasattr(report, 'wasxfail')
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         file_name = report.nodeid.replace("::", "_") + ".png"
    #         _capture_screenshot(file_name)
    #         if file_name:
    #             html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
    #                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
    #             extra.append(pytest_html.extras.html(html))
    #     report.extra = extra
    if report.when in ('setup', 'call'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{report.nodeid.replace('::', '_').replace('/', '_')}_{timestamp}.png"
            driver = getattr(item._request.cls, 'driver', None)
            if driver:
                screenshot_path = _capture_screenshot(driver, file_name)
                html = (
                    f'<div><img src="{screenshot_path}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
