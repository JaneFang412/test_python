from selenium.webdriver.common.by import By

from appium_xueqiu2.page.base_page import BasePage
from appium_xueqiu2.page.market_page import Market


class Main(BasePage):
    def goto_market(self):
        self.find(By.XPATH, "//*[@text='行情']").click()
        return Market(self._driver)

