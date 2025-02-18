from playwright.sync_api import Page, expect

def test_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/select/single_select')

    select_element = page.locator('[id="id_choose_language"]')
    select_element.select_option('Java')
    page.wait_for_timeout(1500)
    select_element.select_option('1')
    page.wait_for_timeout(1500)
    select_element.select_option(label="C#")
    page.wait_for_timeout(1500)
    select_element.select_option(value="2")
    page.wait_for_timeout(1500)
    select_element.select_option(value="Python")
    page.wait_for_timeout(1500)


