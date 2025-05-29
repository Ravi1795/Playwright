import time

import pytest
from playwright.sync_api import Page, expect

from pages.loginPage import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)  # This will automatically use the setUp fixture for all test methods in the class
    def classMethod(self, setUp):
        """This is automatically called before each test in the class."""
        self.page = setUp  # Automatically using page from the setUp fixture
        self.lp = LoginPage(self.page)  # Initializing LoginPage with the page object

    def test_valid(self):
        self.lp.valid_login("ravi707@mailinator.com","Rr@778998445665")
        time.sleep(5)
        expect(self.lp.verifyValidLogin).to_have_text("Memories")

