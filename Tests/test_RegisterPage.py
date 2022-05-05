from selenium import webdriver
from Pages.BasePage import BasePage
import pytest


# ---------------TEST CASE VARIABLES-----------------
url = "https://demoqa.com/text-box"
username = "Testing Testingyan"
email = "Testing@test.com"
address1 = "Current Address"
address2 = "Permanent Address"


@pytest.mark.usefixtures('init_driver')
class TestRegisterFlow:
    def test_positive_register(self):
        obj = BasePage(self.driver)
        obj.navigate_by_url(url)
        obj.do_register(username, email, address1, address2)
