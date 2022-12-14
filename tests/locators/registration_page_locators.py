from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NEW_NAME_AND_EMAIL = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//input[contains(@name, 'name')]"  # Регистрация - поля: Имя и email
    NEW_PASSWORD = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//input[contains(@name, 'Пароль')]"  # Регистрация - поле: Пароль
    TEXT_ERROR = By.XPATH, "//p[contains(@class,'input__error')]"  # ошибка "Некорректный пароль"
    BUTTON_SIGN_UP = By.XPATH,  "//button[contains(text(), 'Зарегистрироваться')]"