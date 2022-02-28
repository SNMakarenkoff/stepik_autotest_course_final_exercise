from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'URL не содержит подстроку "login"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма авторизации не найдена'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации не найдена'

    def register_new_user(self, email, password):
        email_area = self.browser.find_element(*LoginPageLocators.EMAIL_AREA)
        email_area.send_keys(email)
        password1_area = self.browser.find_element(*LoginPageLocators.PASSWORD_AREA)
        password1_area.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_AREA)
        password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

