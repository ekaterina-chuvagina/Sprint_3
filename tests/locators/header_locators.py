from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//a[contains(@href, '/account')]"  # кнопка Личный кабинет
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"  # кнопка Конструктор
    LOGO_ST_BURG = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"  # логотип Stellar Burgers
