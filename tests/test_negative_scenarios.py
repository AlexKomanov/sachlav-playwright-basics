from playwright.sync_api import Page, expect
import pytest

test_negative_data = [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("locked_out_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service")
]

@pytest.mark.parametrize("username, password, error_message", test_negative_data)
def test_sauce_demo_negative_login(page: Page, login_page, username: str, password: str, error_message: str):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    login_page.login_to_system(username, password)
    login_page.validate_login_error_message(error_message)
    expect(page).to_have_url(base_url)
    expect(page).to_have_title("Swag Labs")
