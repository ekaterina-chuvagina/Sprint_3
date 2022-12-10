import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import LoginPageLocators, HeaderLocators

main_page_url = 'https://stellarburgers.nomoreparties.site/'
login_page_url = 'https://stellarburgers.nomoreparties.site/login'
account_profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'


# Переход по клику в Личный кабинет с главной страницы без авторизации
def test_transitions_account_profile_user_not_authorized_in_page_login(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # ожидание для загрузки страницы
    time.sleep(3)

    current_url = driver.current_url

    assert current_url == login_page_url


# Переход по клику в Личный кабинет с главной страницы с авторизацией
def test_transitions_account_profile_user_authorized_in_page_account_profile(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    # найти и нажать на кнопку "Войти в аккаунт"
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_changes(main_page_url))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # ожидание для загрузки страницы
    time.sleep(3)

    current_url = driver.current_url

    assert current_url == account_profile_page_url


# Переход из Личного кабинета по клику на «Конструктор»
def test_transitions_from_account_profile_in_constructor_user_authorized_in_page_main(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    # найти и нажать на кнопку "Войти в аккаунт"
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # найти и нажать на кнопку Конструктор
    driver.find_element(*HeaderLocators.BUTTON_CONSTRUCTOR).click()

    # ожидание для загрузки страницы
    time.sleep(3)

    current_url = driver.current_url

    assert current_url == main_page_url


# Переход из Личного кабинета по клику на логотип Stellar Burgers
def test_transitions_from_account_profile_in_logo_user_authorized_in_page_main(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    # найти и нажать на кнопку "Войти в аккаунт"
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # найти и нажать на логотип
    driver.find_element(*HeaderLocators.LOGO_ST_BURG).click()

    # ожидание для загрузки страницы
    time.sleep(3)

    current_url = driver.current_url

    assert current_url == main_page_url
