import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, close_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestParam():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('searchkey, type, exp_price', [
        ('alibaba', 'BABA', 90),
        ('xiaomi', '01810', 11)
    ])
    def test_param(self, searchkey, type, exp_price):
        '''
        1.打开雪球 应用
        2. 点击搜索框
        3. 输入搜索词 ‘alibaba' or 'xiaomi'...
        4. 点击第一个搜索结果
        5. 判断股票价格

        :return:
        '''
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        cur_price = self.driver.find_element(MobileBy.XPATH,
                                             f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text

        assert_that(float(cur_price), close_to(exp_price, exp_price*0.1))
