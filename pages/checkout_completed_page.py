from playwright.sync_api import Page, expect

class CheckoutCompletedPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__pony_express = page.locator("[data-test=\"pony-express\"]")
        self.__back_to_products = page.locator("[data-test=\"back-to-products\"]")
        self.__title = page.locator("[data-test=\"title\"]")
        self.__complete_header = page.locator("[data-test=\"complete-header\"]")
        self.__complete_text = page.locator("[data-test=\"complete-text\"]")
        self.__primary_header = page.locator("[data-test=\"primary-header\"]")

    def verify_order_completion(self):
        expect(self.__pony_express).to_be_visible()
        expect(self.__back_to_products).to_be_visible()
        expect(self.__title).to_contain_text("Checkout: Complete!")
        expect(self.__complete_header).to_contain_text("Thank you for your order!")
        expect(self.__complete_text).to_contain_text(
            "Your order has been dispatched, and will arrive just as fast as the pony can get there!")
        expect(self.__primary_header).to_match_aria_snapshot("- text: Swag Labs")

    def return_to_products(self):
        self.__back_to_products.click()
