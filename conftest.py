import pytest

from selene import browser
print('hello')

@pytest.fixture(scope="session")
def screen_resolution():
    browser.config.window_height = 1024
    browser.config.window_width = 1920
    yield
    browser.quit()
@pytest.fixture(scope="session")
def browser_open():
    browser.open('https://duckduckgo.com/')


