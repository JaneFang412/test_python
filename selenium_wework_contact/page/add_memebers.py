from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AddMembers:
    def __init__(self, driver:WebDriver):
        self._driver = driver

    def add_memeber(self):
        #username  memberAdd_acctid  memberAdd_phone
        # sleep(3)
        self._driver.find_element(By.ID, 'username').send_keys("abf")
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("abf")
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("11111111116")
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        # sleep(4)
        # self._driver.quit()
        return True

    def get_memebers(self):
        # .member_colRight_memberTable_td:nth-child(2)
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        list = []
        for element in elements:
            list.append(element.get_attribute("title"))

        return list


