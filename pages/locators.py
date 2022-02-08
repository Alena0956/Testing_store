from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '.header__icon-container.header__icon-container_person')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_container')
	REGISTER_FORM = (By.CSS_SELECTOR, '.d-flex.flex-column.align-items-start.login__registration')

