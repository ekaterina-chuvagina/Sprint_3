from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NEW_NAME_AND_EMAIL = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//input[contains(@name, 'name')]"  # Регистрация - поля: Имя и email
    NEW_PASSWORD = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//input[contains(@name, 'Пароль')]"  # Регистрация - поле: Пароль
    AUTH_BUTTON_LOCATOR = By.XPATH, "//button[contains(@class, 'button_button')]"  # кнопка Зарегистрироваться
    TEXT_ERROR = By.XPATH, "//*[contains(@class,'input__error text_type_main-default')]"  # ошибка "Некорректный пароль"


class LoginPageLocators:
    EMAIL_FIELD = By.XPATH, "//form[starts-with(@class, 'Auth_form')]//input[contains(@name, 'name')]"
    PASSWORD_FIELD = By.XPATH, "//form[starts-with(@class, 'Auth_form')]//input[contains(@name, 'Пароль')]"
    BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE = By.XPATH, "//button[contains(@class, 'button_button')]"  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_ENTER = By.XPATH, "//button[contains(@class, 'button_button')]"  # кнопка "Войти"
    BUTTON_ENTER_FORM_REGISTRATION = By.XPATH, "//a[contains(@href, '/login')]" # кнопка "Войти" в форме регистрации


class ForgotPasswordLocators:
    AUTH_LINK = By.XPATH, "//div[starts-with(@class, 'Auth_login')]//a[contains(@href, '/login')]"


class HeaderLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//a[contains(@href, '/account')]"  # кнопка Личный кабинет
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"  # кнопка Конструктор
    LOGO_ST_BURG = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]"  # логотип Stellar Burgers


class AccountProfilePageLocators:
    BUTTON_LOGOUT = By.XPATH, "//button[contains(@class, 'Account_button')]"  # кнопка Выйти


class SectionConstructorLocators:
    BUNS = By.XPATH, "//div[contains(@class, 'tab_tab')]//span[contains(text(), 'Булки')]"
    SAUCES = By.XPATH, "//div[contains(@class, 'tab_tab')]//span[contains(text(), 'Соусы')]"
    TOPPINGS = By.XPATH, "//div[contains(@class, 'tab_tab')]//span[contains(text(), 'Начинки')]"
    CURRENT_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span" # текущая вкладка
