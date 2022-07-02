from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.maximize_window()
        #隐式等待,作用于全局，所以放在setup方法中
        self.driver.implicitly_wait(3)


    def test_wait(self):
        self.driver.find_element(By.LINK_TEXT, '热门').click()
        #强制等待3秒sleep(3)
        # sleep(3)
        #显示等待，先定义一个方法，这个方法需要被传递到显示等待中
        # def wait(x):
        #     # xpath=//th[contains(.,'话题')]
        #     return len(self.driver.find_elements(By.XPATH, '//th[contains(.,"话题")]'))>=1
        # WebDriverWait(self.driver, 10).until(wait)

        #expected_conditions 判断元素是否出现,显示等待一起使用.
        #xpath=//th[contains(.,'回复 ')]
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, '精华帖')))
        self.driver.find_element(By.LINK_TEXT, '【每日一题20220331】列表运算').click()
