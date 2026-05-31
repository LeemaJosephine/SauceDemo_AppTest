"""
Test execution happens here
"""
import allure
import pytest

from PageObjects.HomePage import HomePage1
from TestData.config import SauceDemoData
from Utilities.excel_function import Excelfunction
from Utilities.logger import LogGen

# Read data from Excel
excel = Excelfunction(SauceDemoData.file_name, SauceDemoData.login_sheet_name)
login_data = excel.get_data_from_excel()

class TestLogin:

    logger = LogGen.loggen()

    @allure.feature("Login Feature")
    @allure.story("Validate login with valid and invalid credentials")
    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password, test_type, expected_result", login_data)
    def test_login(self,setup_browser, username, password, test_type, expected_result):
        self.logger.info("Test case started")
        driver = setup_browser
        self.logger.info("Browser Launched")
        assert HomePage1(driver).login(username, password, test_type , expected_result) == True
        self.logger.info("Test case completed")
        print("SUCCESS: Login works")
        self.logger.info("Login Successful")