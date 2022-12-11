from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.header_locators import HeaderLocators
from locators.login_page_locators import LoginPageLocators
from constants import Constants


def test_main_page_login_via_login_button_user_logged_in_successfully(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    # найти и нажать на кнопку "Войти в аккаунт"
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_changes(Constants.MAIN_PAGE_URL))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).text

    assert button_text == 'Оформить заказ'



def test_main_page_login_via_account_button_user_logged_in_successfully(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_changes(Constants.MAIN_PAGE_URL))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).text

    assert button_text == 'Оформить заказ'




