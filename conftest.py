import pytest
from selene import browser

@pytest.fixture(scope='session')
def test_browser_resolution():
    browser.config.window_width = 768
    browser.config.window_height = 1440

@pytest.fixture(scope='session')
def test_browser_wb():
    browser.open('https://www.wildberries.ru')

@pytest.fixture(scope='session')
def test_browser_dd():
    browser.open('https://duckduckgo.com/')
