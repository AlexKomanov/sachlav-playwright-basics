from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://devexpress.github.io/testcafe/example/")
    expect(page.get_by_role("banner")).to_contain_text("This webpage is used as a sample in TestCafe tutorials.")
    page.get_by_test_id("name-input").press_sequentially("alexnader")
    page.get_by_test_id("remote-testing-checkbox").check()
    page.get_by_test_id("reusing-js-code-checkbox").check()
    page.get_by_test_id("reusing-js-code-checkbox").uncheck()
    page.get_by_test_id("parallel-testing-checkbox").check()
    page.get_by_test_id("ci-checkbox").check()
    page.get_by_test_id("analysis-checkbox").check()
    page.get_by_test_id("tried-testcafe-checkbox").check()
    page.get_by_test_id("macos-radio").check()
    page.get_by_test_id("preferred-interface-select").select_option("Both")
    page.locator("#slider").click(position={"x": 160, "y": 5})
    page.locator("#slider").click(position={"x": 700, "y": 5})

    page.get_by_test_id("comments-area").fill("ddddddddddddd")
    page.get_by_test_id("submit-button").click()
    expect(page.get_by_test_id("thank-you-header")).to_contain_text("Thank you, alexnader!")

    page.wait_for_timeout(1500)