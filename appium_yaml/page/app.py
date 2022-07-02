from appium import webdriver

from appium_yaml.page.basepage import BasePage
from appium_yaml.page.main import Main

'''
desird_caps['appPackage']='com.xueqiu.android'
desird_caps['appActivity']='com.xueqiu.android.common.MainActivity'
'''
class App(BasePage):
    def start(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0'
            # NAB0220916007307  127.0.0.1:7555
            desired_caps['deviceName'] = '127.0.0.1:7555'
            # desired_caps['automationName'] = 'UiAutomator2'
            # automationName = UiAutomator2
            # adb shell dumpsys window | findstr mCurrentFocus
            # com.tencent.wework/com.tencent.wework.launch.WwMainActivity
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
            # .launch.LaunchSplashActivity
            desired_caps['noReset'] = True
            desired_caps['skipServerInstallation'] = True
            desired_caps['skipDeviceInitialization'] = True
            # desired_caps['unicodeKeyBoard'] = 'true'
            # desired_caps['resetKeyBoard'] = 'true'
            # desired_caps['chromedriverExecutable'] = 'D:/BrowserDriver/appium_chrome/chromedriver.exe'
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)

        return self

    def main(self) -> Main:
        return Main(self._driver)