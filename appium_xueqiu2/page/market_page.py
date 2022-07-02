from selenium.webdriver.common.by import By

from appium_xueqiu2.page.base_page import BasePage
from appium_xueqiu2.page.search_page import Search


class Market(BasePage):
    def goto_search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)
