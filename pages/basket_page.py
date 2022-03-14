from .main_page import MainPage
from .locators import BasketPageLocators

class BasketPage(MainPage):
	def basket_should_be_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
		'The basket is not empty'

	def should_be_message_about_emty_basket(self):
		assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
		 "Message isn't presented, but should be"