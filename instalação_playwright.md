
#<b>playwright install </b>

Add Example Test
Create a file that follows the test_ prefix convention, such as test_example.py, inside the current working directory or in a sub-directory with the code below. Make sure your test name also follows the test_ prefix convention.
<b>test_example.py</b>

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
<b>Running the Example Test</b>

By default tests will be run on chromium. This can be configured via the CLI options. Tests are run in headless mode meaning no browser UI will open up when running the tests. Results of the tests and test logs will be shown in the terminal.

pytest


<b>Updating Playwright</b>
To update Playwright to the latest version run the following command:

pip install pytest-playwright playwright -U

