"""
Contains all the locators
"""

class BaseLocator:

    username ="user-name" #id
    password ="password" #id
    submit = "login-button" # id

    # Validate login
    product_page ="//span[text()='Products']" #Xpath
    login_error ="//h3[@data-test='error']"  #Xpath