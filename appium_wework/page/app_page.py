
from appium import webdriver

from appium_wework.page.basepage import Base
from appium_wework.page.main_page import Main


class App(Base):
    #capability self._driver初始化
    #启动被测试的app
    def start(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0'
            # NAB0220916007307  127.0.0.1:7555
            desired_caps['deviceName'] = 'NAB0220916007307'
            desired_caps['automationName'] = 'UiAutomator2'
            # automationName = UiAutomator2
            # adb shell dumpsys window | findstr mCurrentFocus
            # com.tencent.wework/com.tencent.wework.launch.WwMainActivity
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            # .launch.LaunchSplashActivity
            desired_caps['noReset'] = True
            desired_caps['skipServerInstallation'] = True
            desired_caps['skipDeviceInitialization'] = True
            # desired_caps['unicodeKeyBoard'] = 'true'
            # desired_caps['resetKeyBoard'] = 'true'
            # desired_caps['chromedriverExecutable'] = 'D:/BrowserDriver/appium_chrome/chromedriver.exe'
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        else:
            #启动被测app（具体的参数会自动读取上面的内容）
            self._driver.launch_app()
        #隐式等待
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass
    def stop(self):
        self._driver.quit()

    #和main_page关联
    def main(self)-> Main:
        return Main(self._driver)