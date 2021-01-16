from selenium.webdriver.common.by import By


class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "basket-items")
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner>p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group [href*='basket/']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    ADDED_TO_BASKET_NAME_MSG = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    ADDED_TO_BASKET_PRICE_MSG = (By.CSS_SELECTOR, "#messages .alert-info strong")
