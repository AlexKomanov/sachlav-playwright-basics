from playwright.sync_api import Page, expect
import pytest
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

test_data = [
    (os.getenv("STANDARD_USER"), os.getenv("SECRET_SAUCE")),
    (os.getenv("PERFORMANCE_GLITCH_USER"), os.getenv("SECRET_SAUCE")),
    (os.getenv("ERROR_USER"), os.getenv("SECRET_SAUCE")),
    (os.getenv("PROBLEM_USER"), os.getenv("SECRET_SAUCE")),
    (os.getenv("VISUAL_USER"), os.getenv("SECRET_SAUCE")),
]

@pytest.mark.parametrize("username, password", test_data)
def test_login_with_success(page: Page, username: str, password: str):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")