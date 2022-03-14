from .main_page import MainPage
from .locators import ProductPageLocators

class ProductPage(MainPage):
	def add_to_basket_button(self):
		basket = self.browser.find_element(*ProductPageLocators. BUTTON_ADD_TO_BASKET)
		basket.click()

	def check_success_message(self):
		assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		'Success message is not presented, but should be'

	def check_product_name(self):
		name = self.browser.find_element(*ProductPageLocators. PRODUCT_NAME)
		alert_name = self.browser.find_element(*ProductPageLocators. ALERT_NAME)
		print(name.text, '- it is simple name')
		print(alert_name.text, '- it is name in alert')
		assert alert_name.text == name.text, 'The name in the basket does not match,\
		maybe other product was added to basket'

	def check_product_price(self):
		price = self.browser.find_element(*ProductPageLocators. PRICE_PRODUCT).text
		alert_price = self.browser.find_element(*ProductPageLocators. ALERT_PRICE).text
		print(price, '= it is simple price')
		print(alert_price, '= it is price in alert')
		assert alert_price == price, 'The price in the basket does not match'