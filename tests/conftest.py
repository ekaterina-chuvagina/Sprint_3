import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=900,800')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

