from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import ForgotPasswordLocators, LoginPageLocators

forgot_password_page_url = 'https://stellarburgers.nomoreparties.site/forgot-password'


def test_forgot_password_page_login_button_user_logged_in_successfully(driver):

    # перейти в форму регистрации
    driver.get(forgot_password_page_url)

    # найти и нажать на кнопку "Войти"
    driver.find_element(*ForgotPasswordLocators.AUTH_LINK).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_changes(forgot_password_page_url))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(forgot_password_page_url))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN_ACCOUNT_MAIN_PAGE).text

    assert button_text == 'Оформить заказ'
