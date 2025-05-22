from selene import browser, be, have

text = 'фваполрвапрвроапвапроывап'

def test_browser_search(screen_resolution, browser_open):
    browser.element('[name="q"]').should(be.blank).type('selenium').press_enter()
    browser.element('[class="kY2IgmnCmOGjharHErah"]').should(have.text(' is a software project that allows you to automate web applications using various browsers. Learn how to use '))
def test_browser_unsearch(screen_resolution, browser_open):
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('html').should(have.text('По запросу «фваполрвапрвроапвапроывап» ничего не найдено.'))

