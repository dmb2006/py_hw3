from selene import browser, be, have

def test_find_search(test_browser_resolution, test_browser):
    browser.element('[type="search"]').should(be.blank).type(have.text('star wars')).press_enter()
    browser.element('[id="c213739936"]').click()
