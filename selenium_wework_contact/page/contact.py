from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_contact.page.add_memebers import AddMembers


class Contact():
    def __init__(self, driver:WebDriver):
        self._driver = driver

    def goto_addmemeber(self):
        #.js_has_member>div:nth-child(1) .js_add_memeber
        #>子元素， “ ”空格，既可以是子元素又可以是孙子元素
        #'.js_has_memeber>div:nth-child(1)>a:nth-child(2)'
        locator = (By.CSS_SELECTOR, '.js_add_member:nth-child(2)')
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))
        self._driver.find_element(By.CSS_SELECTOR, '.js_add_member:nth-child(2)').click()
        return AddMembers(self._driver)



