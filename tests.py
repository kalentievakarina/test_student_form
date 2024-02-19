from selene import browser, have, be, query

def test_user_name():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.get(query.title)
   browser.element('#firstName').should(be.blank)
   browser.element('#firstName').type('Miu').press_enter()

def test_user_lastName():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#lastName').should(be.blank)
   browser.element('#lastName').type('Mui').press_enter()
def test_user_email():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#userEmail').should(be.blank)
   browser.element('#userEmail').type('new@email.com').press_enter()

def test_user_gender():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#gender-radio-1').press()
   browser.element('#gender-radio-2').press()
   browser.element('#gender-radio-3').press()

def test_user_number():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#userNumber').should(be.blank)
   browser.element('#userNumber').type('1234567890').press_enter()

def test_user_birhday():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#dateOfBirthInput').press_enter()

def test_user_subject():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#subjectsInput').type('M').press_enter()
   browser.element('#subjectsInput').type('che').press_enter()
   browser.element('#subjectsInput').type('commerce').press_enter()
   browser.element('#subjectsInput').press_enter()

def test_hobby():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#hobbiesWrapper').element('#hobbies-checkbox-1').press()
   browser.element('#hobbiesWrapper').element('#hobbies-checkbox-2').press()
   browser.element('#hobbiesWrapper').element('#hobbies-checkbox-3').press()

def test_picture():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#uploadPicture').context_click()


def test_adress():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#currentAddress').should(be.blank)
   browser.element('#currentAddress').type('takay-to street, 92').press_enter()


def test_city():
   browser.open('https://demoqa.com/automation-practice-form')
   browser.element('#stateCity-wrapper').element('#state').element('#react-select-3-input').press()
   browser.element('#stateCity-wrapper').element('#city').element('#react-select-4-input').press()

def test_submit_button():
      browser.open('https://demoqa.com/automation-practice-form')
      browser.element('#submit').should(have.exact_text('Submit'))
      browser.element('#submit').press()


