from playwright.sync_api import Page, expect


def test_type_text_into_input(page: Page):
    # Resize viewport for individual page
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto('https://www.qa-practice.com/elements/input/simple')

    text_input_element = page.get_by_placeholder('Submit me')
    expect(text_input_element).to_have_attribute('required', '')
    expect(text_input_element).to_have_attribute('id', 'id_text_string')

    text_to_validate = "alexander_komanov"
    text_input_element.fill(text_to_validate)
    text_input_element.press('Enter')

    expect(page.locator('[id="result-text"]')).to_have_text(text_to_validate)
    page.wait_for_timeout(1000)

