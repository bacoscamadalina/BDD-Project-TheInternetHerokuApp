import time

from driver import Driver
from selenium.webdriver.common.by import By


class BasePage(Driver):
    # Declaram constantele ce contin selectorii: tuple
    URL = 'https://the-internet.herokuapp.com/login'
    USER_LOC = (By.XPATH, '//input[@name="username"]')
    PASS_LOC = (By.ID, 'password')
    BUTTON_LOC = (By.CSS_SELECTOR, '[class="fa fa-2x fa-sign-in"]')
    SECURE_LOC = (By.XPATH, '//h2')

    # Definim metodele de interactionare cu elementele HTML
    def navigate_to_login(self):
        self.driver.get(self.URL)
        time.sleep(2)

    # Definim metodele de validare
    def enter_username(self):
        self.driver.find_element(*self.USER_LOC).send_keys('tomsmith')
        time.sleep(2)

    def enter_password(self):
        self.driver.find_element(*self.PASS_LOC).send_keys('SuperSecretPassword!')
        time.sleep(2)

    def click_login_button(self):
        self.driver.find_element(*self.BUTTON_LOC).click()
        time.sleep(2)

    def validate_secure(self):
        msg = self.driver.find_element(*self.SECURE_LOC).text
        print(msg)
        expected_msg = 'Secure Area'
        assert expected_msg in msg, ' We are not in the secure area'

    def validate_url(self):
        URL2 = 'https://the-internet.herokuapp.com/secure'
        assert self.driver.current_url == URL2, 'Page is incorrect '

    def enter_invalid(self, username, password):
        self.driver.find_element(*self.USER_LOC).send_keys(username)
        self.driver.find_element(*self.PASS_LOC).send_keys(password)

    def validate_sameURL(self):
        assert self.driver.current_url == self.URL
