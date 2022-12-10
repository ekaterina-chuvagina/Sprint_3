import time
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from tests.locators import RegistrationPageLocators, LoginPageLocators
from tests.helpers import generate_login

registration_page_url = 'https://stellarburgers.nomoreparties.site/register'
login_page_url = 'https://stellarburgers.nomoreparties.site/login'


def test_registration_page_user_should_be_registered_successfully(driver):
    username = generate_login()
    email = username + "@yandex.ru"

    driver.get(registration_page_url)

    # Имя и email
    nameAndEmail = driver.find_elements(*RegistrationPageLocators.NEW_NAME_AND_EMAIL)
    nameAndEmail[0].send_keys(username)
    nameAndEmail[1].send_keys(email)

    # Пароль
    driver.find_element(*RegistrationPageLocators.NEW_PASSWORD).send_keys("123456")

    # Найди кнопку "Регистрации" и кликни по ней
    driver.find_element(*RegistrationPageLocators.AUTH_BUTTON_LOCATOR).click()

    # ожидание для загрузки страницы
    time.sleep(3)

    current_url = driver.current_url

    assert current_url == login_page_url


@pytest.mark.parametrize("password", ["a", "abc", "abcde"])
def test_registration_page_password_with_incorrect_number_of_characters_should_show_error(driver, password):
    username = generate_login()
    email = username + "@yandex.ru"

    driver.get(registration_page_url)

    # Имя и email
    nameAndEmail = driver.find_elements(*RegistrationPageLocators.NEW_NAME_AND_EMAIL)
    nameAndEmail[0].send_keys(username)
    nameAndEmail[1].send_keys(email)

    # Пароль
    driver.find_element(*RegistrationPageLocators.NEW_PASSWORD).send_keys(password)

    # Найди кнопку "Регистрации" и кликни по ней
    driver.find_element(*RegistrationPageLocators.AUTH_BUTTON_LOCATOR).click()

    # явное ожидание для загрузки ошибки
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'input__error')))
    errorText = driver.find_element(*RegistrationPageLocators.TEXT_ERROR).text

    assert errorText == 'Некорректный пароль'


def test_registration_page_login_button_user_logged_in_successfully(driver):

    # перейти в форму регистрации
    driver.get(registration_page_url)

    # найти и нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER_FORM_REGISTRATION).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_changes(registration_page_url))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_changes(registration_page_url))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).text

    assert button_text == 'Оформить заказ'
