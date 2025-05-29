import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")


@pytest.fixture(scope="session")
def setUp(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "safari":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise Exception("Invalid Browser Name")
    new_context = browser.new_context()
    page = new_context.new_page()
    page.goto("https://www.mystoriesmatter.com/")
    yield page
    browser.close()
