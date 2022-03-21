
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .locators import ContactUsPageLocators
from selenium.webdriver.support.ui import Select
import time

class MainPage():
	def __init__(self, browser, url, timeout = 10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def open(self):
		self.browser.get(self.url)

	def go_to_login_page(self):
		link = self.browser.find_element(*MainPageLocators. LOGIN_LINK)
		link.click()

	def go_to_basket(self):
		link = self.browser.find_element(*MainPageLocators. VIEW_BASKET)
		link.click()

	# метод, который проверяет присутствует ли элемент на странице
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True
		
	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators. LOGIN_LINK), \
		'Login link is not presented'

	# метод, который проверяет, что элемент не появляется на странице в течение заданного времени		
	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False

	def should_be_authorized_user(self):
		assert self.is_element_present(*MainPageLocators.USER_ICON), \
		"User icon is not presented, probably unauthorised user" 

	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators. LOGIN_LINK), \
		'Login link is not presented'

	def go_to_contact_us(self):
		link = self.browser.find_element(*MainPageLocators. CONTACT_US)
		link.click()

	def sending_message(self):
		subject = Select(self.browser.find_element(*ContactUsPageLocators. SUBJECT))
		subject.select_by_value("2")
		email = self.browser.find_element(*ContactUsPageLocators. EMAIL)
		email.send_keys(str(time.time()) + '@gmail.com')
		message = self.browser.find_element(*ContactUsPageLocators. MESSAGE)
		message.send_keys('I can not track my order. Where is it?')
		button = self.browser.find_element(*ContactUsPageLocators. BUTTON_SEND)
		button.click()

	def should_be_success_message(self):
		assert self.is_element_present(*ContactUsPageLocators. ALERT_SUCCESS), \
		'Success message is not presented'










