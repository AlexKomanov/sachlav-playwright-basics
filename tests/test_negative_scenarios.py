from playwright.sync_api import Page, expect
import pytest
import data.login_data as ld

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

test_negative_data = [
    (ld.LOCKED_OUT_USER, os.getenv("SECRET_SAUCE"), "Epic sadface: Sorry, this user has been locked out."),
    (ld.LOCKED_OUT_USER, ld.WRONG_PASSWORD, "Epic sadface: Username and password do not match any user in this service")
]

@pytest.mark.parametrize("username, password, error_message", test_negative_data)
def test_sauce_demo_negative_login(page: Page, login_page, username: str, password: str, error_message: str):
    page.goto(ld.BASE_URL)
    login_page.login_to_system(username, password)
    login_page.validate_login_error_message(error_message)
    expect(page).to_have_url(ld.BASE_URL)
    expect(page).to_have_title("Swag Labs")
