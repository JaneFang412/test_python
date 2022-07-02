from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_wework_main.page.add_memeber import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    # _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_memeber(self):
        #click add memeber
        # index_service_cnt_item_title
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()

        # self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self._driver)