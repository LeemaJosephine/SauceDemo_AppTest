"""
Store all the static data here
"""
import os


class SauceDemoData:

    base_url = "https://www.saucedemo.com"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(BASE_DIR, "..", "TestData" , "TestData.xlsx")

    # Login
    login_sheet_name = "LoginTest"

