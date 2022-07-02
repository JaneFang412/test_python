import time

from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebView():
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
        desired_caps['chromedriverExecutable'] = 'D:/BrowserDriver/appium_chrome/chromedriver.exe'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(25)


    def teardown(self):
        time.sleep(20)
        self.driver.quit()
        # pass

    def test_webviewer(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        create_Acc = (MobileBy.XPATH, '//android.view.View[@content-desc="去开户"]')
        # print(self.driver.contexts)
        # #切换到webveiw页面，也就是切换上下文
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # time.sleep(10)
        # print(self.driver.window_handles)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(create_Acc))
        self.driver.find_element(*create_Acc).click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.window_handles)
        # kaihu_window = self.driver.window_handles[-1]
        # self.driver.switch_to.window(kaihu_window)

        phone_num = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(phone_num))
        self.driver.find_element(*phone_num).send_keys("13555944127")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="code"]').send_keys("123456")
        self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="立即开户"]').click()
