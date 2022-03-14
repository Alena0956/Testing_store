from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.actions_of_registered_user
class TestUserCanAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		login_link = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
		page = LoginPage(browser, login_link)
		page.open()
		email = str(time.time()) + "@gmail.com"
		password = str(time.time()) + "passWORD"
		page.register_new_user(email, password)
		page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = 'http://automationpractice.com/index.php?id_product=1&controller=product'
		page = ProductPage(browser, link)
		page.open()
		page.add_to_basket_button()
		time.sleep(7)
		page.check_success_message()
		page.check_product_name()
		page.check_product_price()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
		link = 'http://automationpractice.com/index.php?id_product=1&controller=product'
		page = ProductPage(browser, link)
		page.open()
		page.add_to_basket_button()
		time.sleep(7)
		page.check_success_message()
		page.check_product_name()
		page.check_product_price()

@pytest.mark.need_review_2
def test_guest_can_go_to_login_page_from_product_page(browser):
 	link = "http://automationpractice.com/index.php?id_product=2&controller=product"
 	page = LoginPage(browser, link)
 	page.open()
 	page.go_to_login_page()
 	time.sleep(5)
 	page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://automationpractice.com/index.php?id_product=2&controller=product"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()




