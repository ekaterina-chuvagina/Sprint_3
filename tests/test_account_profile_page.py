from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.account_profile_page_locators import AccountProfilePageLocators
from locators.header_locators import HeaderLocators
from locators.login_page_locators import LoginPageLocators
from constants import Constants


# Проверка выхода по кнопке «Выйти» в личном кабинете
def test_account_profile_page_logout_button_user_authorized_in_page_login(driver):
    # перейти на страницу login
    driver.get(Constants.LOGIN_PAGE_URL)

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.LOGIN_PAGE_URL))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Constants.ACCOUNT_PROFILE_PAGE_URL))

    # найти и нажать на кнопку "Выйти"
    button = driver.find_element(*AccountProfilePageLocators.BUTTON_LOGOUT)
    button.click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(Constants.ACCOUNT_PROFILE_PAGE_URL))

    current_url = driver.current_url

    assert current_url == Constants.LOGIN_PAGE_URL
