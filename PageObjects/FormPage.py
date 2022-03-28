from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    radiobutton = (By.ID, "inlineRadio2")
    dob = (By.NAME, "bday")


    def getFirstname(self):
        return self.driver.find_element(*FormPage.firstName)

    def getEmail(self):
        return self.driver.find_element(*FormPage.email)

    def getPassword(self):
        return self.driver.find_element(*FormPage.password)

    def getCheckbox(self):
        return self.driver.find_element(*FormPage.checkbox)

    def getGender(self):
        return self.driver.find_element(*FormPage.gender)

    def getButton(self):
        return self.driver.find_element(*FormPage.radiobutton)

    def getDOB(self):
        return self.driver.find_element(*FormPage.dob)





