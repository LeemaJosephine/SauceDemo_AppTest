import allure
import pytest
from selenium import webdriver

from TestData.config import SauceDemoData

@allure.step("Take screenshot and attach to Allure report")
def capture_screenshot(driver,step_name):
    allure.attach(driver.get_screenshot_as_png(),
                  name = step_name,
                  attachment_type=allure.attachment_type.PNG
                  )

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get(SauceDemoData.base_url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.close()
