class TimelinePage:

    def __init__(self, page):
        self.page = page

    # locators
    addMemory = "//button[@class='styled__StyledButton-sc-1edb4g-3 bMIAwn']"
    memoryTitle = "//input[@id='memory-title']"
    memoryBody = ".tiptap.ProseMirror"
    publishCTA = "//button[@id='msm-publish-button']"
    timelineToggle = "//span[normalize-space()='Timeline']"
    cuesSelect = ".Cue__CueContainer-sc-1vnbk6z-0.gFgAKX"

    def clickAddMemory(self):
        self.page.locator(self.addMemory).nth(-1).click()

    def addTitle(self, title):
        self.page.locator(self.memoryTitle).fill(title)

    def addMemoryBody(self, body):
        self.page.locator(self.memoryBody).fill(body)

    def clickPublishCTA(self):
        self.page.locator(self.publishCTA).click()

    @property
    def verifyMemoryPublish(self):
        return self.page.locator(self.timelineToggle)

    def clickCues(self):
        self.page.locator(self.cuesSelect).nth(-1).click()

    def clickNewMemory(self):
        self.page.get_by_role("button", name="New memory").click()

    def timelinePage(self, tt, bb, skip_add_memory=False):
        if not skip_add_memory:  # This is skipped if `skip_add_memory=True`
            self.clickAddMemory()
        self.addTitle(tt)
        self.addMemoryBody(bb)
        self.clickPublishCTA()

    def newCueMemory(self, tt, bb):
        self.clickCues()
        self.clickNewMemory()
        self.timelinePage(tt, bb, skip_add_memory=True)
