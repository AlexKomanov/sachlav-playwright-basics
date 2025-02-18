from playwright.sync_api import Page, expect

def test_check(page: Page):
    page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    checkbox_0 = page.get_by_role('checkbox', name='Select me or not')
    checkbox_0.click()
    page.wait_for_timeout(3000)
    checkbox_0.click()

    page.wait_for_timeout(3000)

    checkbox_0.check()
    page.wait_for_timeout(3000)
    checkbox_0.check()
    page.wait_for_timeout(3000)
    checkbox_0.uncheck()

