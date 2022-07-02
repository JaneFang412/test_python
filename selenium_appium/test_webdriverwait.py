import time
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestDW():
    #初始化设置
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("search test case")
        '''
        1.打开雪球app
        2.点击搜索框
        3.向搜索框输入 "阿里巴巴"
        4.在搜索结果里面选择“阿里巴巴”，然后进行点击
        4.获得阿里巴巴估计，价格大于200
        '''
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/title_container']//*[@text='股票']").click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele = self.driver.find_element(*locator)
        print(ele.text)
        curr_price = float(ele.text)
        expected_price = 85
        # assert curr_price>expected_price
        #区间是(expected_price + expected_price*0.1) - expected_price*0.1
        assert_that(curr_price, close_to(expected_price, expected_price*0.1))
