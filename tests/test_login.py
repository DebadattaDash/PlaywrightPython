import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    # page.get_by_title("Help").click()
    page.get_by_alt_text("profile picture").click()
    page.get_by_text("Logout").click()
    page.wait_for_timeout(10000)