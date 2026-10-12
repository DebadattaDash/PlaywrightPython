import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Below are css selectors flow:
    # page.locator("input[placeholder='Username']").fill("Admin")
    # page.locator("input[placeholder='Password']").fill("admin123")
    # page.locator("button[type='submit']").click()
    # # page.get_by_title("Help").click()
    # page.wait_for_timeout(10000)


    #below are xpath flow:
    page.locator("//input[@placeholder='Username']").fill("Admin")
    page.locator("//input[@placeholder='Password']").fill("admin123")
    page.locator("//button[normalize-space()='Login']").click()
    page.locator("//img[@class='oxd-userdropdown-img']").click()
    page.locator("(//a[normalize-space()='Logout'])[1]").click()
    page.wait_for_timeout(5000)
