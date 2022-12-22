from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.header_locators import HeaderLocators
from locators.login_page_locators import LoginPageLocators
from constants import Constants


def test_main_page_login_via_login_button_user_logged_in_successfully(driver):
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
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_MAKE_ORDER).text

    assert button_text == 'Оформить заказ'


def test_main_page_login_via_account_button_user_logged_in_successfully(driver):
    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Личный кабинет"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(HeaderLocators.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.LOGIN_PAGE_URL))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER))
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_MAKE_ORDER).text

    assert button_text == 'Оформить заказ'
