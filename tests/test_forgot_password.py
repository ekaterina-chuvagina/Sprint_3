from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.login_page_locators import LoginPageLocators
from constants import Constants


def test_forgot_password_page_login_button_user_logged_in_successfully(driver):

    # перейти в форму регистрации
    driver.get(Constants.FORGOT_PASSWORD_PAGE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.FORGOT_PASSWORD_PAGE_URL))

    # найти и нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(ForgotPasswordLocators.AUTH_LINK))
    driver.find_element(*ForgotPasswordLocators.AUTH_LINK).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.LOGIN_PAGE_URL))

    # ввести email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys("user1234@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("qwerty")

    # нажать на кнопку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER))
    driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    # явное ожидание для загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))

    button_text = driver.find_element(*LoginPageLocators.BUTTON_MAKE_ORDER).text

    assert button_text == 'Оформить заказ'
