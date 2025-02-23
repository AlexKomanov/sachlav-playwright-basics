from playwright.sync_api import Page, expect
import pytest
from test_data import constants as const

@pytest.mark.cart
def test_added_items(page: Page, login_page, products_page):
    """Test adding multiple items to cart and verifying cart badge count"""
    # Navigate and login
    page.goto(const.BASE_URL)
    login_page.login_to_system(const.STANDARD_USER, const.SECRET_SAUCE)
    
    # Verify successful login
    expect(page).to_have_url(const.INVENTORY_URL)
    
    # Add all items to cart and verify badge count
    products_page.add_all_items_to_cart()
    products_page.go_to_cart()
