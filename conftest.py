import pytest
from selene import browser

@pytest.fixture(scope="session")
def screen_resolution():
    browser.config.window_height = 1024
    browser.config.window_width = 768
    yield
    browser.quit()

