from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_link_text("United Kingdom").click()
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    # self.driver.find_element_by_css_selector("[type='submit']").click()

    link_text = (By.LINK_TEXT, "United Kingdom")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")

    def LinkTxt(self):
        return self.driver.find_element(*ConfirmPage.link_text)

    def Checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def Submit(self):
        return self.driver.find_element(*ConfirmPage.submit)
