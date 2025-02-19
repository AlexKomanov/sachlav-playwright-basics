from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page: Page):
        self.__username_textfield = page.locator("[data-test=\"username\"]")
        self.__password_textfield = page.locator("[data-test=\"password\"]")
        self.__login_button = page.locator("[data-test=\"login-button\"]")
        self.__error_message_element = page.locator("[data-test=\"error\"]")


    def type_username(self, username: str):
        self.__username_textfield.fill(username)

    def type_password(self, password: str):
        self.__password_textfield.fill(password)

    def click_login_button(self):
        self.__login_button.click()

    def login_to_system(self, username: str, password: str):
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()

    def validate_login_error_message(self, error_message: str):
        expect(self.__error_message_element).to_contain_text(error_message)


