
from .locators import LoginPageLocators
from .main_page import MainPage

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
        assert '/profile' in self.browser.current_url, 'Login is not present in url'

    # проверка наличия формы регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators. REGISTER_FORM), 'Register form is not presented'
    