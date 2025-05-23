from selene import browser, be, have

def test_find_search(test_browser_resolution, test_browser_wb):
    browser.element('[type="search"]').should(be.blank).type('star wars').press_enter()
    browser.element('[id="c314332073"]').click()

def test_find_unsearch(test_browser_resolution, test_browser_dd):
    browser.element('[name="q"]').should(be.blank).type('ываолрфварпварпвапыва').press_enter()
    browser.element('html').should(have.text('По запросу «ываолрфварпварпвапыва» ничего не найдено.'))

