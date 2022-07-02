from appium import webdriver

from appium_xueqiu2.page.base_page import BasePage
from appium_xueqiu2.page.main_page import Main


class App(BasePage):
    '''
    @desciption: 启动要测试的app和页面
    @return:返回值：self，用于去其他类继续调用
    @
    '''
    def start(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            desired_caps['noReset'] = True
            desired_caps['skipServerInstallation'] = True
            desired_caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(15)
        return self

    def stop(self):
        self._driver.quit()

    def main(self)-> Main:
        return Main(self._driver)







