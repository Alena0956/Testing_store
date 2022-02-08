
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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

	# метод, который проверяет присутствует ли элемент на странице
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True
		
	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators. LOGIN_LINK), 'Login link is not presented'
