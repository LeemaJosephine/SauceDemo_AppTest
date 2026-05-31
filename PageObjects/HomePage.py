"""
Contains all the methods relevant to home page
"""
import allure
from selenium.webdriver.common.by import By

from TestLocators.locators import BaseLocator
from conftest import capture_screenshot


class HomePage1:

    def __init__(self,driver):
        self.driver = driver

    #Homepage relevant methods
    @allure.step("Login with username: {1} and password: {2}")
    def login(self,username,password,test_type,expected_result):

        self.driver.find_element(By.ID,value=BaseLocator.username).send_keys(username)
        self.driver.find_element(By.ID,value=BaseLocator.password).send_keys(password)
        self.driver.find_element(By.ID,value=BaseLocator.submit).click()

        if test_type == "ValidUsernameValidPassword":
            actual_text = self.driver.find_element(By.XPATH,value=BaseLocator.product_page).text
            capture_screenshot(self.driver,"SucessfulLogin")
            assert actual_text == expected_result , f"Expected: {expected_result}, Actual: {actual_text}"

        elif test_type == "InvalidUsernameValidPassword":
            actual_text = self.driver.find_element(By.XPATH,value=BaseLocator.login_error).text
            capture_screenshot(self.driver, "InvalidUsernameValidPassword")
            assert actual_text == expected_result, f"Expected: {expected_result}, Actual: {actual_text}"

        elif test_type == "ValidUsernameInvalidPassword":
            actual_text = self.driver.find_element(By.XPATH, value=BaseLocator.login_error).text
            capture_screenshot(self.driver, "ValidUsernameInvalidPassword")
            assert actual_text == expected_result, f"Expected: {expected_result}, Actual: {actual_text}"

        elif test_type == "InvalidUsernameInvalidPassword":
            actual_text = self.driver.find_element(By.XPATH, value=BaseLocator.login_error).text
            assert actual_text == expected_result, f"Expected: {expected_result}, Actual: {actual_text}"

        elif test_type == "BlankUsername":
            actual_text = self.driver.find_element(By.XPATH, value=BaseLocator.login_error).text
            assert actual_text == expected_result, f"Expected: {expected_result}, Actual: {actual_text}"

        elif test_type == "BlankPassword":
            actual_text = self.driver.find_element(By.XPATH, value=BaseLocator.login_error).text
            assert actual_text == expected_result, f"Expected: {expected_result}, Actual: {actual_text}"

        return True


