class LoginPage:
    def __init__(self, page):
        self.page = page

    # locators
    loginCTA = "//span[contains(.,'Log in')]"
    continueWithEmailCTA = "//span[normalize-space()='Continue with email']"
    email = "//input[@placeholder='Enter your email...']"
    passWord = "//input[@placeholder='Enter your password...']"
    continueCTA = "//span[normalize-space()='Continue']"
    validLogin = "//p[normalize-space()='Memories']"
    logoutCTA = "//p[normalize-space()='Logout']"

    def clickLogin(self):
        self.page.locator(self.loginCTA).click()

    def continueWithEmail(self):
        self.page.locator(self.continueWithEmailCTA).click()

    def enterUsername(self, username):
        self.page.locator(self.email).fill(username)

    def enterPassword(self, password):
        self.page.locator(self.passWord).fill(password)

    def clickContinue(self):
        self.page.locator(self.continueCTA).click()

    @property
    def verifyValidLogin(self):
        return self.page.locator(self.validLogin)

    def valid_login(self, username, password):
        """Performs valid login using username and password."""
        self.clickLogin()
        self.continueWithEmail()
        self.enterUsername(username)
        self.clickContinue()
        self.enterPassword(password)
        self.clickContinue()
