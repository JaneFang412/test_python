from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions
import pytest
from selenium.webdriver.common.by import By

class TestTouchAction():
    def setup(self):
        #执行报错,需要设置w3c
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_touchaction_scroolbottom(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element(By.ID, "kw")
        el_search = self.driver.find_element(By.ID, "su")
        el.send_keys("selenium")
        sleep(3)
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el, 0, 10000)
        action.perform()
        sleep(5)





