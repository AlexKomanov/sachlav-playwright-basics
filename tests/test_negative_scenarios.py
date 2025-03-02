from playwright.sync_api import Page, expect
import pytest
from test_data import constants as const
import allure

test_negative_data = [
    (const.LOCKED_OUT_USER, const.SECRET_SAUCE, const.LOCKED_OUT_ERROR),
    (const.LOCKED_OUT_USER, const.WRONG_PASSWORD, const.INVALID_CREDENTIALS_ERROR)
]

@pytest.mark.sanity
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("username, password, error_message", test_negative_data)
def test_sauce_demo_negative_login(page: Page, login_page, username: str, password: str, error_message: str):
    """Test login failures with invalid credentials and locked out user"""
    # Navigate to the application
    with allure.step(f"Navigating to page with url: '{const.BASE_URL}'"):
        page.goto(const.BASE_URL)
    
    # Attempt login with invalid credentials
    login_page.login_to_system(username, password)
    
    # Verify error messages and page state
    login_page.validate_login_error_message(error_message)
    expect(page).to_have_url(const.BASE_URL+"/")
    expect(page).to_have_title("Swag Labs")
