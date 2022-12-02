from browser import Browser
from imports import *

'''
a. Home page https://the-internet.herokuapp.com/
- Sa aiba cel putin 3 elemente inlcusiv Form Authentication
- Sa contina metode de click pe ele
'''

class HomePage(Browser):
    
    FORM_AUTH_LINK = (By.LINK_TEXT, "Form Authentication")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password")
    BASIC_AUTH_LINK = (By.LINK_TEXT, "Basic Auth")


    def navigate_to_home_page(self):
        self.driver.get("https://the-internet.herokuapp.com")

    def click_to_form_auth(self):
        self.driver.find_element(*self.FORM_AUTH_LINK).click()

    def click_to_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def click_to_basic_auth(self):
        self.driver.find_element(*self.BASIC_AUTH_LINK).click()