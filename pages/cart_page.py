from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.__checkout_button = page.locator("[data-test=\"checkout\"]")

    def proceed_to_checkout(self):
        self.__checkout_button.click()
