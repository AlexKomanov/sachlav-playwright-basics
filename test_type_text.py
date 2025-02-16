from playwright.sync_api import Page, expect


def test_type_text(page: Page):
    # Resize viewport for individual page
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto('https://www.qa-practice.com/elements/textarea/single')

    # page.locator('[name="text_area"]').fill('AAAaaaaaaaaaa')
    text_box_element = page.get_by_role('textbox')
    text_box_element.fill('AAAaaaaaaaaaa')
    page.wait_for_timeout(1000)
    text_box_element.fill('Alexander Komanov')
    page.wait_for_timeout(1000)

    text_box_element.press_sequentially("New Text New Text")
    page.wait_for_timeout(1000)
    text_box_element.clear()

    text_to_validate = "Another Another Another"
    text_box_element.press_sequentially(text_to_validate, delay=100)


    page.locator('[id="submit-id-submit"]').click(timeout=5000)

    expect(page.locator('[id="result"]')).to_be_visible()
    expect(page.locator('[id="result"] p').first).to_have_text("You entered")
    expect(page.locator('[id="result"]').locator('[id="result-text"]')).to_have_text(text_to_validate)

    page.wait_for_timeout(1000)

