import pytest
from selene import browser, be


@pytest.fixture(scope="session")
def screen_resolution():
    browser.config.window_height = 1024
    browser.config.window_width = 1920

@pytest.fixture(scope="session")
def browser_open():
    print('Браузер открыт')
    browser.open('https://duckduckgo.com/')
    yield
    browser.quit()
    print('Браузер закрыт')

