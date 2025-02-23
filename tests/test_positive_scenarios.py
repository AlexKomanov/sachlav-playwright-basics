from playwright.sync_api import Page, expect
import pytest
from test_data import constants as const

test_data = [
    (const.STANDARD_USER, const.SECRET_SAUCE),
    (const.PERFORMANCE_GLITCH_USER, const.SECRET_SAUCE),
    (const.ERROR_USER, const.SECRET_SAUCE),
    (const.PROBLEM_USER, const.SECRET_SAUCE),
    (const.VISUAL_USER, const.SECRET_SAUCE),
]

@pytest.mark.login
@pytest.mark.positive
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_success(page: Page, login_page, username: str, password: str):
    """Test successful login with different valid user credentials"""
    # Navigate to the application
    page.goto(const.BASE_URL)
    
    # Login with credentials
    login_page.login_to_system(username, password)
    
    # Verify successful login
    expect(page).to_have_url(const.INVENTORY_URL)