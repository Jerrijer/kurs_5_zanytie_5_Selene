import os
from selene.support.shared import browser
from selene import have

def test_55(browser_management):


# имя фамилия майл
        browser.open('/automation-practice-form')
        browser.element('#firstName').type('Evgeniy')
        browser.element('#lastName').type('А')
        browser.element('#userEmail').type('EvgeniyA@yandex.ru')

# пол, телефон
        browser.element('#gender-radio-1')
        browser.element('#userNumber').type('9037077077')

# дата рождения
        browser.element('.react-datepicker-wrapper').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="1991"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('[value="6"]').click()
        browser.element('.react-datepicker__day--006').click()


# предмет и хобби
        browser.element('#subjectsInput').type('Eco').press_enter()
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()

# загрузка картинки

       # browser.element('[id=uploadPicture]').send_keys(os.getcwd() + ('/CAT.jpg')

# адресс
        browser.element('#currentAddress').click().type(
        '11111, г. Москва,  ш. Новое  200')
        browser.element('#state #react-select-3-input').type('NCR').press_enter()
        browser.element('#city #react-select-4-input').type('Del').press_enter()

# отправить
        browser.element('#submit').press_enter()


...
