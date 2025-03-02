from playwright.sync_api import Page, expect
import pytest
from test_data import constants as const
import allure

test_data = [
    (const.STANDARD_USER, const.SECRET_SAUCE),
    (const.PERFORMANCE_GLITCH_USER, const.SECRET_SAUCE),
    (const.ERROR_USER, const.SECRET_SAUCE),
    (const.PROBLEM_USER, const.SECRET_SAUCE),
    (const.VISUAL_USER, const.SECRET_SAUCE),
]

@pytest.mark.login
@pytest.mark.positive
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.sanity
@pytest.mark.parametrize("username, password", test_data)
@allure.severity(severity_level=allure.severity_level.MINOR)
@allure.title("Positive Scenario with user '{username}'")
def test_login_with_success(page: Page, login_page, username: str, password: str):
    allure.description("Test successful login with different valid user credentials")
    allure.dynamic.parent_suite("Sanity")
    allure.dynamic.suite("Module X")
    allure.dynamic.sub_suite("Feature xyz")
    # Navigate to the application
    with allure.step(f"Navigating to page with url: '{const.BASE_URL}'"):
        page.goto(const.BASE_URL)
    
    # Login with credentials
    login_page.login_to_system(username, password)
    
    # Verify successful login
    expect(page).to_have_url(const.INVENTORY_URL)