from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            #io.appium.android.apis
            #com.example.android.apis
            'appPackage': 'com.example.android.apis',
            'appActivity': 'com.example.android.apis.ApiDemos',
            'deviceName': '192.168.56.101:5555',
            # 'noReset': True,
            'chromedriverExecutable': "D:/BrowserDriver/appium_chrome/chromedriver.exe"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}")'
                                                        '.instance(0));').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i has no focus').send_keys("this is a test string")
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i am a link').click()
        print(self.driver.page_source)
