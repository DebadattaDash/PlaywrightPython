import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    expect(page.get_by_role("heading", name="Playwright CLI")).to_be_visible()
    expect(page.get_by_role("main")).to_match_aria_snapshot("- heading \"Built for testing\" [level=2]\n- heading \"Auto-wait and web-first assertions\" [level=4]\n- paragraph: Playwright waits for elements to be actionable before performing actions. Assertions automatically retry until conditions are met. No artificial timeouts, no flaky tests.\n- heading \"Test isolation\" [level=4]\n- paragraph: Each test gets a fresh browser context — equivalent to a brand new browser profile. Full isolation with near-zero overhead. Save authentication state once and reuse it across tests.\n- heading \"Resilient locators\" [level=4]\n- paragraph:\n  - text: \"Find elements with selectors that mirror how users see the page:\"\n  - code: getByRole\n  - text: \",\"\n  - code: getByLabel\n  - text: \",\"\n  - code: getByPlaceholder\n  - text: \",\"\n  - code: getByTestId\n  - text: . No brittle CSS paths.\n- heading \"Parallelism and sharding\" [level=4]\n- paragraph: Tests run in parallel by default across all configured browsers. Shard across multiple machines for faster CI. Full cross-browser coverage on every commit.")
