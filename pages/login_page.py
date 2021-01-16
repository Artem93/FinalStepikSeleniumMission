from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        assert self.set_text_to_element(email, *LoginPageLocators.EMAIL_FIELD), "trouble with sending email"
        assert self.set_text_to_element(password, *LoginPageLocators.PASS1_FIELD), "trouble with sending password 1"
        assert self.set_text_to_element(password, *LoginPageLocators.PASS2_FIELD), "trouble with sending password 1"
        assert self.click_to_element(*LoginPageLocators.REG_BTN), "trouble with clicking reg button"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current URL not contains 'login'"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True