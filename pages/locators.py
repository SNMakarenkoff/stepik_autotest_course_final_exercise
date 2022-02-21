from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    BOOK_NAME_CHECK = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE_CHECK = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) div.alertinner')
    OPEN_PRODUCT_PAGE = (By.CSS_SELECTOR, '[title="Coders at Work"]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
