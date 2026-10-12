from playwright.sync_api import Page,expect

def test_js_alert(page:Page):
    page.goto(
        "https://the-internet.herokuapp.com/javascript_alerts",
        wait_until="domcontentloaded",
        timeout=60000
    )
    expect(page.get_by_role("heading", name="JavaScript Alerts")).to_be_visible()
    page.once("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(3000)
    page.get_by_text("Click for JS Alert").click()
    page.wait_for_timeout(5000)
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")
    page.wait_for_timeout(3000)

def test_js_confirmation_cancel(page: Page):
    page.goto(
        "https://the-internet.herokuapp.com/javascript_alerts",
        wait_until="domcontentloaded",
        timeout=60000
    )
    expect(page.get_by_role("heading", name="JavaScript Alerts")).to_be_visible()
    page.once("dialog", lambda dialog: dialog.dismiss())
    # we are saying playwright when this event occurs u need to create an annonimous function then you need to dismiss that dialogue
    page.wait_for_timeout(3000)
    page.get_by_text("Click for JS Confirm").click()
    page.wait_for_timeout(5000)
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")
    page.wait_for_timeout(3000)

def test_js_prompt_text(page: Page):
    page.goto(
        "https://the-internet.herokuapp.com/javascript_alerts",
        wait_until="domcontentloaded",
        timeout=60000
    )
    expect(page.get_by_role("heading", name="JavaScript Alerts")).to_be_visible()
    page.once("dialog", lambda dialog: dialog.accept("Playwright Python Demo"))
    page.wait_for_timeout(3000)
    page.get_by_text("Click for JS Prompt").click()
    page.wait_for_timeout(5000)
    expect(page.locator("#result")).to_have_text("You entered: Playwright Python Demo")
    page.wait_for_timeout(3000)


