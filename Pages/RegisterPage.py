from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class RegisterPage(BasePage):
    USERNAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    def do_register(self, username, email, address1, address2):
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.EMAIL_INPUT, email)
        self.do_send_keys(self.CURRENT_ADDRESS_INPUT, address1)
        self.do_send_keys(self.PERMANENT_ADDRESS_INPUT, address2)
        self.do_click(self.SUBMIT_BUTTON)
