from pages.TimelinePage import TimelinePage


class PromptPage:

    def __init__(self, page):
        self.page = page
        self.tl = TimelinePage(page)

    # locators
    prompts = "a[class='Navbar__NavItem-sc-bpaubx-9 kMgztt'] p[class='typography__Body-sc-1rnknoa-5 cTmoDC']"
    selectPrompt = ".PromptCard__PromptCardWrapper-sc-ugk9r0-1.yrTRP"
    promptTitle = "p[data-testid='promptbanner-title']"
    visibility = ".typography__Title2-sc-1rnknoa-2.styled__CardTitle-sc-yfmyxx-18.iwRHaL.icZIov.ph-no-capture"
    timelineToggle = ".typography__Title3-sc-1rnknoa-3.eKjfJP"
    recentPage ="//span[normalize-space()='Recent']"

    def clickPromptSection(self):
        self.page.locator(self.prompts).click()

    def clickPrompt(self):
        self.page.locator(self.selectPrompt).nth(0).click()

    @property
    def verifyPrompt(self):
        self.page.locator(self.visibility).nth(0).wait_for(state="visible")
        return self.page.locator(self.visibility).nth(0)

    def clickToggle(self):
        self.page.get_by_label("Feed").click()
        self.page.get_by_text("Recent").click()

    def Prompts(self, tt, bb):
        self.clickPromptSection()
        self.clickPrompt()
        self.tl.timelinePage(tt, bb,skip_add_memory=True)
        self.clickToggle()
