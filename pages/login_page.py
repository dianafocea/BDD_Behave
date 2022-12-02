from imports import *


'''
b. Login page https://the-internet.herokuapp.com/login
- Sa contina user, pass, login_btn si metode pt interactiune cu ele
'''

class LoginPage(HomePage):

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "fa-sign-in")
    ERROR_MESSAGE_INVALID_USERNAME = (By.ID, "flash")

    def navigate_to_login_page(self):
        self.click_to_form_auth()


    def set_username(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_username_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_INVALID_USERNAME).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect, expected {expected_message}, actual {actual_message}'


