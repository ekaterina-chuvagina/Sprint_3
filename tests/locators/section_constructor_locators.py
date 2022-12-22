from selenium.webdriver.common.by import By


class SectionConstructorLocators:
    BUNS = By.XPATH, "//div[contains(@class, 'tab_tab') and span[contains(text(), 'Булки')]]"
    SAUCES = By.XPATH, "//div[contains(@class, 'tab_tab') and span[contains(text(), 'Соусы')]]"
    TOPPINGS = By.XPATH, "//div[contains(@class, 'tab_tab') and span[contains(text(), 'Начинки')]]"
    CURRENT_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span" # текущая вкладка
