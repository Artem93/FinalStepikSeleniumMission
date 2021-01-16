from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        btn_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        self.should_be_name_message()
        self.should_be_price_message()

    def should_be_name_message(self):
        if self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_NAME_MSG):
            assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_NAME_MSG).text, \
                "Message not contains product name"
        else:
            assert False, "Message with name is not presented"

    def should_be_price_message(self):
        if self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_PRICE_MSG):
            assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRICE_MSG).text, \
                "Basket price not equal product price"
        else:
            assert False, "Message with price is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_PRICE_MSG), "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_PRICE_MSG), "Success message is presented, but should not be"
