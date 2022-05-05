from Pages.BasePage import BasePage
import pytest
from selenium import webdriver


def __init__(self, driver):
    BasePage.__init__(self, driver)


@pytest.fixture()
def set_up(self):
    path = 'driver/chromedriver.exe'
    self.driver = webdriver.Chrome(path)
    self.driver.maximize_window()
    yield
    self.driver.close()


# ---------------TEST CASE VARIABLES-----------------
url = "https://demoqa.com/text-box"
username = "Testing Testingyan"
email = "Testing@test.com"
address1 = "Current Address"
address2 = "Permanent Address"


@pytest.mark.usefixtures('set_up')
class TestRegisterFlow:
    def test_positive_register(self):
        obj = BasePage(self.driver)
        obj.navigate_by_url(url)
        obj.do_register(username, email, address1, address2)
