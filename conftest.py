import pytest
from selene import browser

@pytest.fixture()
def test_browser_resolution():
    browser.config.window_width = 1440
    browser.config.window_height = 768

@pytest.fixture()
def test_browser():
    browser.open('https://www.wildberries.ru')


