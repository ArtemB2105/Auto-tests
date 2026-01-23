from playwright.sync_api import Page, expect


def test_wiki(page: Page):
    page.goto("https://ru.wikipedia.org/")
    page.get_by_role(role="link", name="Содержание").click()
    expect(page.locator("#firstHeading")).to_have_text("Википедия:Содержание")
