
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators

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


