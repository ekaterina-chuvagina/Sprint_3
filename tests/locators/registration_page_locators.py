from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NEW_NAME_AND_EMAIL = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//input[contains(@name, 'name')]"  # Регистрация - поля: Имя и email
    NEW_PASSWORD = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//input[contains(@name, 'Пароль')]"  # Регистрация - поле: Пароль
    AUTH_BUTTON_LOCATOR = By.XPATH, "//button[contains(@class, 'button_button')]"  # кнопка Зарегистрироваться
    TEXT_ERROR = By.XPATH, "//*[contains(@class,'input__error text_type_main-default')]"  # ошибка "Некорректный пароль"
