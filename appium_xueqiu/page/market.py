import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.basepage import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)
