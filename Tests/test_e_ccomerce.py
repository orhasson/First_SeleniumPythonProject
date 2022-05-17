import time
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()

        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Nokia Edge":
                checkoutpage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()  ## checkout button
        checkoutitem = checkoutpage.checkOutItems()
        log.info("Entering country name as 'united ki'")
        self.driver.find_element_by_id("country").send_keys("united ki")
        time.sleep(5)
        self.verifyLinkPresence("United Kingdom")

        checkoutpage.LinkTxt().click()
        checkoutpage.Checkbox().click()
        checkoutpage.Submit().click()

        textCompare = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("The Text is " + textCompare)

        assert ("Success! Thank you!" in textCompare)
