from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = By.XPATH, "//form[starts-with(@class, 'Auth_form')]//input[contains(@name, 'name')]"
    PASSWORD_FIELD = By.XPATH, "//form[starts-with(@class, 'Auth_form')]//input[contains(@name, 'Пароль')]"
    BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_ENTER = By.XPATH, "//button[contains(text(), 'Войти')]"  # кнопка "Войти"
    BUTTON_ENTER_FORM_REGISTRATION = By.XPATH, "//a[contains(text(), 'Войти')]" # кнопка "Войти" в форме регистрации
    BUTTON_MAKE_ORDER = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
