from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//header//nav//a[contains(@href, '/account')]"  # кнопка Личный кабинет
    BUTTON_CONSTRUCTOR = By.XPATH, "//header//nav//ul/li/a[@href='/']"  # кнопка Конструктор
    LOGO_ST_BURG = By.XPATH, "//header//nav//div[contains(@class, 'AppHeader_header__logo')]//a"  # логотип Stellar Burgers
