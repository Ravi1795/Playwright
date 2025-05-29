from datetime import datetime

import pytest
from playwright.sync_api import expect

from pages.Prompts import PromptPage


class TestCues:

    @pytest.fixture(autouse=True)
    def classMethod(self, setUp):
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.page = setUp
        self.pp = PromptPage(self.page)

    def test_verifyPrompt(self):
        title = "Created from prompt during Smoke testing on " + self.date
        body = "This is a test body content for the memory created from prompts during Smoke testing on " + self.date
        self.pp.Prompts(title, body,)
        expect(self.pp.verifyPrompt).to_contain_text("Created from prompt")
