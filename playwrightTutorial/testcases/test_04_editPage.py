import pytest

from pages.editPage import EditPage


class TestEditPage:

    @pytest.fixture(autouse=True)
    def classMethod(self, setUp):
        self.page = setUp
        self.ep = EditPage(self.page)

    def test_verifyEditPage(self):
        nn = "Test collection created during smoke testing"
        self.ep.editPageCheck(nn)
