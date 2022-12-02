from imports import *
from pages.login_page import LoginPage

'''
c. Secure page https://the-internet.herokuapp.com/secure
- Sa contina mesajul de succes si verificare ca e displayed
- Sa contina logout_btn si click pe el
'''

class SecureLoginPage(LoginPage):

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-signout")
    LOGIN_NOTIFICATION_MESSAGE = (By.ID, "flash")

    def navigate_to_secure_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/secure")


    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def display_login_notification_message(self, expected_message):
        self.set_username('tomsmith')
        self.set_password('SuperSecretPassword!')
        self.click_login_button()
        try:
            actual_message = self.driver.find_element(*self.LOGIN_NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect, expected {expected_message}, actual {actual_message}'

    def verify_notification_is_displayed(self):
        notification = self.driver.find_element(*self.LOGIN_NOTIFICATION_MESSAGE).text
        assert notification.is_displayed(), f'Error, notification is not displayed'
