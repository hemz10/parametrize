import pytest
from selenium.webdriver.support.select import Select
from PageObjects.FormPage import FormPage
from Testdata.test_dataDriven import TestData
from Utilities.baseclass import BaseClass


class Test_Form(BaseClass):
    def test_command(self, getData):
        fp = FormPage(self.driver)
        fp.getFirstname().click()
        fp.getFirstname().send_keys(getData['name'])
        fp.getEmail().send_keys(getData["email"])
        fp.getPassword().send_keys(getData["password"])
        fp.getCheckbox().click()
        s = Select(fp.getGender())
        s.select_by_visible_text(getData["gender"])
        fp.getButton().click()
        fp.getDOB().click()
        fp.getDOB().send_keys(getData["dob"])
        self.driver.get_screenshot_as_file(getData["screenshot"])
        self.driver.refresh()


    @pytest.fixture(params=TestData.data)
    def getData(self, request):
        return request.param




