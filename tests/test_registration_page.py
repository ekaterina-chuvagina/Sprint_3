import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators.login_page_locators import LoginPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from helpers import generate_login
from constants import Constants


def test_registration_page_user_should_be_registered_successfully(driver):
    username = generate_login()
    email = username + "@yandex.ru"

    driver.get(Constants.REGISTRATION_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.REGISTRATION_PAGE_URL))

    # Имя и email
    nameAndEmail = driver.find_elements(*RegistrationPageLocators.NEW_NAME_AND_EMAIL)
    nameAndEmail[0].send_keys(username)
    nameAndEmail[1].send_keys(email)

    # Пароль
    driver.find_element(*RegistrationPageLocators.NEW_PASSWORD).send_keys("123456")

    # Найди кнопку "Регистрации" и кликни по ней
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegistrationPageLocators.BUTTON_SIGN_UP))
    driver.find_element(*RegistrationPageLocators.BUTTON_SIGN_UP).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Constants.LOGIN_PAGE_URL))

    current_url = driver.current_url

    assert current_url == Constants.LOGIN_PAGE_URL


@pytest.mark.parametrize("password", ["a", "abc", "abcde"])
def test_registration_page_password_with_incorrect_number_of_characters_should_show_error(driver, password):
    username = generate_login()
    email = username + "@yandex.ru"

    driver.get(Constants.REGISTRATION_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.REGISTRATION_PAGE_URL))

    # Имя и email
    nameAndEmail = driver.find_elements(*RegistrationPageLocators.NEW_NAME_AND_EMAIL)
    nameAndEmail[0].send_keys(username)
    nameAndEmail[1].send_keys(email)

    # Пароль
    driver.find_element(*RegistrationPageLocators.NEW_PASSWORD).send_keys(password)

    # Найди кнопку "Регистрации" и кликни по ней
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegistrationPageLocators.BUTTON_SIGN_UP))
    driver.find_element(*RegistrationPageLocators.BUTTON_SIGN_UP).click()

    # явное ожидание для загрузки ошибки
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'input__error')))
    errorText = driver.find_element(*RegistrationPageLocators.TEXT_ERROR).text

    assert errorText == 'Некорректный пароль'


def test_registration_page_login_button_user_logged_in_successfully(driver):

    # перейти в форму регистрации
    driver.get(Constants.REGISTRATION_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.REGISTRATION_PAGE_URL))

    # найти и нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER_FORM_REGISTRATION))
    driver.find_element(*LoginPageLocators.BUTTON_ENTER_FORM_REGISTRATION).click()

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
