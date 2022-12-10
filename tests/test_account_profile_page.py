from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import LoginPageLocators, HeaderLocators, AccountProfilePageLocators

account_profile_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'
login_page_url = 'https://stellarburgers.nomoreparties.site/login'
main_page_url = 'https://stellarburgers.nomoreparties.site/'


# Проверка выхода по кнопке «Выйти» в личном кабинете
def test_account_profile_page_logout_button_user_authorized_in_page_login(driver):

    # перейти на страницу login
    driver.get(login_page_url)

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(login_page_url))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))

    # найти и нажать на кнопку "Личный кабинет"
    driver.find_element(*HeaderLocators.BUTTON_PERSONAL_ACCOUNT).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(account_profile_page_url))

    # найти и нажать на кнопку "Выйти"
    button = driver.find_element(*AccountProfilePageLocators.BUTTON_LOGOUT)
    button.click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(account_profile_page_url))

    current_url = driver.current_url

    assert current_url == login_page_url
