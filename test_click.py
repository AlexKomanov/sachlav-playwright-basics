from playwright.sync_api import Page, expect

# playwright
# browser
# browser_context
# page

def test_click(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/simple')
    # page.locator('[id="submit-id-submit"]').click() # attribute=value
    # page.locator('#submit-id-submit').click() # css selector
    # page.get_by_text('Click', exact=True).click() # get_by_text
    # page.get_by_text('Click').nth(0).click() # get_by_text + nth
    # page.get_by_role('button', name='Click').click() # get_by_role + name
    page.locator('//input[@id="submit-id-submit"]').click() # xpath
    text_result = page.locator('[id="result-text"]').inner_text()
    # assert text_result == 'Submitted'
    expect(page.locator('[id="result-text"]')).to_contain_text('Submitted', timeout=30000)
    # page.wait_for_timeout(3000)

