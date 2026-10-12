from playwright.sync_api import Page, expect

def test_slider(page: Page):
    page.goto("https://practice-automation.com/slider/")
    page.wait_for_timeout(3000)
    slider = page.locator("#slideMe")
    expect(slider).to_have_value("25")
    slider.fill("80")
    page.wait_for_timeout(3000)
    expect(slider).to_have_value("80")
    slider.fill("0")
    page.wait_for_timeout(3000)
    expect(slider).to_have_value("0")
    slider.fill("100")
    page.wait_for_timeout(3000)
    expect(slider).to_have_value("100")
    #slider.fill("110")
    #page.wait_for_timeout(3000)
    #expect(slider).to_have_value("110")

