from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_AREA = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_AREA = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_AREA = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')

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
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    NO_BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
