"""
Test execution happens here
"""
import allure
import pytest

from PageObjects.HomePage import HomePage1
from TestData.config import SauceDemoData
from Utilities.excel_function import Excelfunction

# Read data from Excel
excel = Excelfunction(SauceDemoData.file_name, SauceDemoData.login_sheet_name)
login_data = excel.get_data_from_excel()

class TestLogin:

    @allure.feature("Login Feature")
    @allure.story("Validate login with valid and invalid credentials")
    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password, test_type, expected_result", login_data)
    def test_login(self,setup_browser, username, password, test_type, expected_result):
        driver = setup_browser
        assert HomePage1(driver).login(username, password, test_type , expected_result) == True
        print("SUCCESS: Login works")