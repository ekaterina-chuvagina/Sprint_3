from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    AUTH_LINK = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//a[contains(@href, '/login')]"
