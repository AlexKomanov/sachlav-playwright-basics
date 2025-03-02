from playwright.sync_api import Page
import pytest
from test_data import constants as const
import allure

@pytest.mark.sanity
@pytest.mark.e2e
def test_end_2_end_scenario(page: Page, login_page, products_page, cart_page, checkout_page, checkout_completed_page):
    """Test complete end-to-end purchase flow from login to checkout"""
    # Navigate to the application
    with allure.step(f"Navigating to page with url: '{const.BASE_URL}'"):
        page.goto(const.BASE_URL)

    # Login with standard user

    login_page.login_to_system(const.STANDARD_USER, const.SECRET_SAUCE)
    
    # Add items to cart and navigate to cart
    products_page.add_all_items_to_cart()
    products_page.go_to_cart()
    
    # Proceed to checkout
    cart_page.proceed_to_checkout()
    
    # Complete checkout process
    checkout_page.fill_information(
        const.CHECKOUT_INFO["first_name"],
        const.CHECKOUT_INFO["last_name"],
        const.CHECKOUT_INFO["postal_code"]
    )
    checkout_page.complete_purchase()
    
    # Verify order completion
    checkout_completed_page.verify_order_completion()
