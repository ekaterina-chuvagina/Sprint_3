from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.section_constructor_locators import SectionConstructorLocators
from constants import Constants


# Проверка перехода к разделу «Соусы»
def test_section_constructor_transition_section_sauces_user_not_authorized_successfully(driver):

    # перейти на главную страницу
    driver.get(Constants.MAIN_PAGE_URL)

    try:
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))
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
    driver.get(Constants.MAIN_PAGE_URL)

    try:
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))
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
    driver.get(Constants.MAIN_PAGE_URL)

    try:
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Constants.MAIN_PAGE_URL))
    except TimeoutException:
        assert False, 'Ошибка при переходе на главную страницу'

    toppings = driver.find_element(*SectionConstructorLocators.TOPPINGS)
    toppings.click()

    buns = driver.find_element(*SectionConstructorLocators.BUNS)
    buns.click()

    current_tab = driver.find_element(*SectionConstructorLocators.CURRENT_TAB)
    current_tab_text = current_tab.text

    assert current_tab_text == 'Булки'