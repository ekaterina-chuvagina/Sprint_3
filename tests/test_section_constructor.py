from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import SectionConstructorLocators

main_page_url = 'https://stellarburgers.nomoreparties.site/'


# Проверка перехода к разделу «Соусы»
def test_section_constructor_transition_section_sauces_user_not_authorized_successfully(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    try:
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))
    except TimeoutException:
        assert False, 'Ошибка при переходе на главную страницу'

    sauces = driver.find_element(*SectionConstructorLocators.SAUCES)
    sauces.click()

    current_tab = driver.find_element(*SectionConstructorLocators.CURRENT_TAB)
    current_tab_text = current_tab.text

    assert current_tab_text == 'Соусы'


# Проверка перехода к разделу «Начинки»
def test_section_constructor_transition_section_toppings_user_not_authorized_successfully(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    try:
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))
    except TimeoutException:
        assert False, 'Ошибка при переходе на главную страницу'

    toppings = driver.find_element(*SectionConstructorLocators.TOPPINGS)
    toppings.click()

    current_tab = driver.find_element(*SectionConstructorLocators.CURRENT_TAB)
    current_tab_text = current_tab.text

    assert current_tab_text == 'Начинки'


# Проверка перехода к разделу «Булки»
def test_section_constructor_transition_section_buns_user_not_authorized_successfully(driver):

    # перейти на главную страницу
    driver.get(main_page_url)

    try:
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(main_page_url))
    except TimeoutException:
        assert False, 'Ошибка при переходе на главную страницу'

    toppings = driver.find_element(*SectionConstructorLocators.TOPPINGS)
    toppings.click()

    buns = driver.find_element(*SectionConstructorLocators.BUNS)
    buns.click()

    current_tab = driver.find_element(*SectionConstructorLocators.CURRENT_TAB)
    current_tab_text = current_tab.text

    assert current_tab_text == 'Булки'