from playwright.sync_api import expect


class EditPage:

    def __init__(self, page):
        self.page = page

    # locators
    editPage = '//p[normalize-space()="Edit"]'
    allMemories = '//span[normalize-space()="All memories"]'
    publishedMemories = '//span[normalize-space()="Published"]'
    draftMemories = '//span[normalize-space()="Drafts"]'
    unsortedMemories = '//span[normalize-space()="Unsorted"]'
    newCollection = "//span[text()='New collection']"
    nameField = "//div[@class='styled__CollectionName-sc-18y1sfc-8 krksrw']/child::input"
    createCollection = "//div[@class='styled__CreateCollectionContainer-sc-18y1sfc-77 iChdkI']/child::div[4]/child::button"
    addMemory = "//span[normalize-space()='Add']"
    backCTA = "//span[text()='Back']"
    collection = "//span[contains(text(),'Test collection')]"
    manageCollection = "//span[normalize-space()='Manage']"
    threeDots = ".styled__DotsContainer-sc-18y1sfc-60.itZIbF"
    deleteCollection = "//p[normalize-space()='Delete Collection']"
    cross = ".ShareMemory__Close-sc-18yq9vl-1.enRxgj"

    def clickEdit(self):
        self.page.locator(self.editPage).click()

    def verifyAllCollections(self):
        expect(self.page.locator(self.allMemories)).to_contain_text("All")
        expect(self.page.locator(self.publishedMemories)).to_contain_text("Published")
        expect(self.page.locator(self.draftMemories)).to_contain_text("Drafts")
        expect(self.page.locator(self.unsortedMemories)).to_contain_text("Unsorted")

    def clickNewCollection(self):
        self.page.locator(self.newCollection).click()

    def enterName(self, name):
        self.page.locator(self.nameField).fill(name)

    def clickAddCollection(self):
        self.page.locator(self.createCollection).click(force=True)

    # def clickAddMemory(self):
    #     self.page.get_by_text("Add", exact=True).nth(0).click()
    #     self.page.get_by_text("Add", exact=True).nth(1).click()

    def clickBack(self):
        self.page.get_by_role('button', name="Back").click()

    def verifyCreatedCollection(self):
        self.page.locator(self.collection).wait_for(state='visible',timeout=20000)
        expect(self.page.locator(self.collection)).to_contain_text("Test collection created")

    def clickCollection(self):
        self.page.locator(self.collection).click()

    def clickManageCollection(self):
        self.page.locator(self.manageCollection).click()

    def clickDeleteCollection(self):
        self.page.locator(self.threeDots).wait_for(state='visible',timeout=20000)
        self.page.locator(self.threeDots).click()
        self.page.locator(self.deleteCollection).click()
        self.page.get_by_role('button',name='Delete collection').click()

    def verifyDelete(self):
        expect(self.page.locator(self.collection)).not_to_be_visible()

    def editPageCheck(self, name):
        self.clickEdit()
        self.verifyAllCollections()
        self.clickNewCollection()
        self.enterName(name)
        self.clickAddCollection()
        self.clickBack()
        self.verifyCreatedCollection()
        self.clickCollection()
        self.clickDeleteCollection()
        self.verifyDelete()
