from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_wework.page.addresslist_page import AddressList

class Main():

    def __init__(self, driver:WebDriver):
        self._driver = driver
    #点击通讯录，进入addresslist_page
    def click_address_list(self):
        # click addresslist button
        self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressList(self._driver)
