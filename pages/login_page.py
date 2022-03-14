
from .locators import LoginPageLocators
from .main_page import MainPage
import time

class LoginPage(MainPage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

	# проверка наличия формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators. LOGIN_FORM), 'Login form is not presented'

    # проверка корректности url адреса
    def should_be_login_url(self):
        assert 'my-account' in self.browser.current_url, 'Login is not present in url'

    # проверка наличия формы регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators. REGISTER_FORM), 'Register form is not presented'

     # регистрация нового пользователя
    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators. EMAIL_ADDRESS)
        email_address.send_keys(email)
        button = self.browser.find_element(*LoginPageLocators. BUTTON_CREATE)
        button.click()
        first_name = self.browser.find_element(*LoginPageLocators. FIRST_NAME)
        first_name.send_keys('Christian')
        last_name = self.browser.find_element(*LoginPageLocators. LAST_NAME)
        last_name.send_keys('Goodman')
        password_field = self.browser.find_element(*LoginPageLocators. REGISTER_PASSWORD)
        password_field.send_keys(password)
        address = self.browser.find_element(*LoginPageLocators. ADDRESS)
        address.send_keys('Main Street, iTest, 343008')
        city = self.browser.find_element(*LoginPageLocators. CITY)
        city.send_keys('Monterey')
        state_list = self.browser.find_element(*LoginPageLocators. STATE)
        state_list.click()
        chosen_state = self.browser.find_element(*LoginPageLocators. CHOSEN_STATE)
        chosen_state.click()
        postal_code = self.browser.find_element(*LoginPageLocators. POSTAL_CODE)
        postal_code.send_keys('34008')
        mobile_phone = self.browser.find_element(*LoginPageLocators. MOBILE)
        mobile_phone.send_keys('080664012')
        button = self.browser.find_element(*LoginPageLocators. BUTTON_REGISTER)
        button.click()
        time.sleep(5)
