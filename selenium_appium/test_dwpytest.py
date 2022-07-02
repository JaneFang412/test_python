import time
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


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

    @pytest.mark.skip
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
        curr_price = float(self.driver.find_element(By.ID, "com.xueqiu.android:id/current_price").text)
        assert curr_price>80

    @pytest.mark.skip
    def test_touch(self):
        sleep(5)
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height*4/5)
        y_end = int(height*1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    @pytest.mark.skip
    def test_cur_price(self):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        cur_price = self.driver.find_element(By.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"current stock price is : {cur_price}")
        assert float(cur_price) > 60

    @pytest.mark.skip
    def test_uiauto(self):
        '''
        1.点击我的，进入个人信息页面
        2点击登录，进入登录页面
        3 输入用户名，输入密码
        4 点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        #多属性定位
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("").test("")')
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        # self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/rl_login']/android.widget.TextView[2]").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        sleep(2)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        sleep(2)

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').click()
        #滚动查找
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("为霜").'
                                                        'instance(0));').click()

        time.sleep(5)




if __name__== '__main__':
    pytest.main()