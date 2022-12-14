from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.header_locators import HeaderLocators
from locators.login_page_locators import LoginPageLocators
from constants import Constants


# Переход по клику в Личный кабинет с главной страницы без авторизации
def test_transitions_account_profile_user_not_authorized_in_page_login(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Личный кабинет"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.LOGIN_PAGE_URL))

    current_url = driver.current_url

    assert current_url == Constants.LOGIN_PAGE_URL


# Переход по клику в Личный кабинет с главной страницы с авторизацией
def test_transitions_account_profile_user_authorized_in_page_account_profile(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Войти в аккаунт"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE))
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.LOGIN_PAGE_URL))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER))
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Личный кабинет"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.ACCOUNT_PROFILE_PAGE_URL))

    current_url = driver.current_url

    assert current_url == Constants.ACCOUNT_PROFILE_PAGE_URL


# Переход из Личного кабинета по клику на «Конструктор»
def test_transitions_from_account_profile_in_constructor_user_authorized_in_page_main(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Войти в аккаунт"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE))
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER))
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Личный кабинет"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.ACCOUNT_PROFILE_PAGE_URL))

    # найти и нажать на кнопку Конструктор
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_CONSTRUCTOR))
    driver.find_element(*HeaderLocators.BUTTON_CONSTRUCTOR).click()

    # ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    current_url = driver.current_url

    assert current_url == Constants.MAIN_PAGE_URL


# Переход из Личного кабинета по клику на логотип Stellar Burgers
def test_transitions_from_account_profile_in_logo_user_authorized_in_page_main(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Войти в аккаунт"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE))
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER))
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Личный кабинет"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.ACCOUNT_PROFILE_PAGE_URL))

    # найти и нажать на логотип
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.LOGO_ST_BURG))
    driver.find_element(*HeaderLocators.LOGO_ST_BURG).click()

    # ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    current_url = driver.current_url

    assert current_url == Constants.MAIN_PAGE_URL
