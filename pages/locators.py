from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '.login')
	VIEW_BASKET = (By.CSS_SELECTOR, '[title="View my shopping cart"]')
	USER_ICON = (By.CSS_SELECTOR, '[title="View my customer account"]')
	LOGIN_LINK = (By.CSS_SELECTOR, '.login')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, '#create-account_form')
	EMAIL_ADDRESS = (By.CSS_SELECTOR, '#email_create')
	BUTTON_CREATE = (By.CSS_SELECTOR, '#SubmitCreate')
	FIRST_NAME = (By.CSS_SELECTOR, '#customer_firstname')
	LAST_NAME = (By.CSS_SELECTOR, '#customer_lastname')
	REGISTER_PASSWORD = (By.CSS_SELECTOR, '#passwd')
	ADDRESS = (By.CSS_SELECTOR, '#address1')
	CITY = (By.CSS_SELECTOR, '#city')
	STATE = (By.CSS_SELECTOR, '#uniform-id_state')
	CHOSEN_STATE = (By.CSS_SELECTOR, '#id_state > option:nth-child(6)')
	POSTAL_CODE = (By.CSS_SELECTOR, '#postcode')
	MOBILE = (By.CSS_SELECTOR, '#phone_mobile')
	BUTTON_REGISTER = (By.CSS_SELECTOR, '#submitAccount')

class BasketPageLocators():
	MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, '.alert.alert-warning')
	BASKET_ITEMS = (By.CSS_SELECTOR,'.cart_item')

class ProductPageLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR,'#add_to_cart')
	ALERT_NAME = (By.CSS_SELECTOR,'.clearfix .layer_cart_product_info .product-name')
	PRODUCT_NAME = (By.CSS_SELECTOR,'.pb-center-column h1')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.layer_cart_product.col-xs-12.col-md-6 h2')
	PRICE_PRODUCT = (By.CSS_SELECTOR, '#our_price_display')
	ALERT_PRICE = (By.CSS_SELECTOR, '#layer_cart_product_price')



