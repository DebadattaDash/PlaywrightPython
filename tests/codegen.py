import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Alex Doe").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    page.wait_for_timeout(5000)