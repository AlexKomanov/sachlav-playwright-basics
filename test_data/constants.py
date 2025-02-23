"""Constants used across the test framework"""

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# URLs
BASE_URL = "https://www.saucedemo.com"
INVENTORY_URL = f"{BASE_URL}/inventory.html"

# Credentials
STANDARD_USER = os.getenv("STANDARD_USER")
PERFORMANCE_GLITCH_USER = os.getenv("PERFORMANCE_GLITCH_USER")
ERROR_USER = os.getenv("ERROR_USER")
PROBLEM_USER = os.getenv("PROBLEM_USER")
VISUAL_USER = os.getenv("VISUAL_USER")
LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER")
SECRET_SAUCE = os.getenv("SECRET_SAUCE")
WRONG_PASSWORD = "wrong_password"

# Error Messages
LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."
INVALID_CREDENTIALS_ERROR = "Epic sadface: Username and password do not match any user in this service"

# Test Data
CHECKOUT_INFO = {
    "first_name": "alex",
    "last_name": "komanov",
    "postal_code": "20100"
}
