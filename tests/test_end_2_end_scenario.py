from playwright.sync_api import Page, expect
import pytest

def test_emd_2_end_scenario(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("alex")
    page.locator("[data-test=\"lastName\"]").fill("komanov")
    page.locator("[data-test=\"postalCode\"]").fill("20100")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    expect(page.locator("[data-test=\"back-to-products\"]")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"complete-text\"]")).to_contain_text(
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    expect(page.locator("[data-test=\"primary-header\"]")).to_match_aria_snapshot("- text: Swag Labs")
