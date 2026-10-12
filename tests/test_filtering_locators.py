import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/v1/index.html")

    # Below are css selectors flow:
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    #create a variable to filter the product
    #product1 = page.locator('.inventory_item_description').filter(has_text="Sauce Labs Bike Light")
    product1 = page.locator('.inventory_item_description').filter(has=page.locator("button.btn_inventory "))
    #product1.locator("button:has-text('Add to cart')").click()
    product1.first.locator("button").click()
    #page.locator("//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    page.wait_for_timeout(15000)

