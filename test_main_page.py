
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

class TestLoginFromMainPage():
	#@pytest.mark.new
	def test_guest_can_go_to_login_page(self, browser):
		link = "http://automationpractice.com/index.php"
		page = MainPage(browser,link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	#@pytest.mark.new
	def test_guest_should_see_login_link(self, browser):
		link = "http://automationpractice.com/index.php"
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()

	#@pytest.mark.new
	def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
		link = "http://automationpractice.com/index.php"
		page = BasketPage(browser,link)
		page.open()
		page.go_to_basket()
		page.basket_should_be_empty()
		page.should_be_message_about_emty_basket()

	@pytest.mark.new
	def test_guest_can_send_message_from_contact_us(self, browser):
		link = "http://automationpractice.com/index.php"
		page = MainPage(browser, link)
		page.open()
		page.go_to_contact_us()
		page.sending_message()
		page.should_be_success_message()
		time.sleep(7)












		

