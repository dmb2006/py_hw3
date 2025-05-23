from selene import browser, be, have

def test_search_positive(test_browser_resolution, test_browser_wb):
    browser.element('[type="search"]').should(be.blank).type('star wars').press_enter()
    browser.element('[id="c314332073"]').click()
    browser.element('html').should(have.text("Световой меч джедая игрушечный"))

def test_search_negative(test_browser_resolution, test_browser_dd):
    browser.element('[name="q"]').should(be.blank).type('ываолрфварпварпвапыва').press_enter()
    browser.element('html').should(have.text('По запросу «ываолрфварпварпвапыва» ничего не найдено.'))
