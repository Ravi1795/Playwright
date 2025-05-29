from datetime import datetime

import pytest
from playwright.sync_api import expect

from pages.TimelinePage import TimelinePage


class TestTimeline:

    @pytest.fixture(autouse=True)
    def classMethod(self, setUp):
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.page = setUp
        self.tl = TimelinePage(self.page)

    def test_timelineMemory(self):
        title = "Created from timeline page during Smoke testing on " + self.date
        body = "This is a test body content for the memory created from timeline page during Smoke testing on " + self.date
        self.tl.timelinePage(title, body)
        expect(self.tl.verifyMemoryPublish).to_contain_text('Timeline')

    def test_cueMemory(self):
        title = "Created from Cues on timeline page during Smoke testing on " + self.date
        body = "This is a test body content for the memory created from cues during Smoke testing on " + self.date
        self.tl.newCueMemory(title, body)
        expect(self.tl.verifyMemoryPublish).to_contain_text('Timeline')
