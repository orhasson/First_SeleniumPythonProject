import pytest

from Excel_Data.HomePageData import HomePageData
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

## testing data input from excel file
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
