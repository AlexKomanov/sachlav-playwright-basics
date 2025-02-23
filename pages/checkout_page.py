from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__first_name = page.locator("[data-test=\"firstName\"]")
        self.__last_name = page.locator("[data-test=\"lastName\"]")
        self.__postal_code = page.locator("[data-test=\"postalCode\"]")
        self.__continue_button = page.locator("[data-test=\"continue\"]")
        self.__finish_button = page.locator("[data-test=\"finish\"]")
        
    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.__first_name.fill(first_name)
        self.__last_name.fill(last_name)
        self.__postal_code.fill(postal_code)
        self.__continue_button.click()

    def complete_purchase(self):
        self.__finish_button.click()

