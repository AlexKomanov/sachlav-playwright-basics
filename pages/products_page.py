from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.__bike_light = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.__fleece_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.__bolt_shirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.__onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.__red_shirt = page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]")
        self.__cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def add_all_items_to_cart(self):
        self.__backpack.click()
        self.__bike_light.click()
        self.__fleece_jacket.click()
        self.__bolt_shirt.click()
        self.__onesie.click()
        self.__red_shirt.click()

    def go_to_cart(self):
        self.__cart_link.click()
