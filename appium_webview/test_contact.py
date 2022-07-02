from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestWeixin():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        #NAB0220916007307  127.0.0.1:7555
        desired_caps['deviceName'] = 'NAB0220916007307'
        desired_caps['automationName'] = 'UiAutomator2'
        #automationName = UiAutomator2
        #adb shell dumpsys window | findstr mCurrentFocus
        #com.tencent.wework/com.tencent.wework.launch.WwMainActivity
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        #.launch.LaunchSplashActivity
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['skipDeviceInitialization'] = True
        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['chromedriverExecutable'] = 'D:/BrowserDriver/appium_chrome/chromedriver.exe'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(80)

    def teardown(self):
        self.driver.quit()

    #获取屏幕尺寸
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return(x, y)
    #向下滑动屏幕
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(1[0] * 0.5) # x坐标
        y1 = int(l[1] *0.5) #y始
        y2 = int(l[1] * 0.9) #y终点
        self.driver.swipe(x1, y1, x1, y2, t)

    def test_add_contract(self):
        print("add a contact")
        sleep(10)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys("appium_t1")
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        #//*[@text="企业邮箱　"]/..//*[@class="android.widget.EditText"]
        self.driver.find_element(MobileBy.XPATH, '//*[@text="企业邮箱　"]/..//*[@class="android.widget.EditText"]').send_keys("appium_t1")
        #//*[@text="手机号"]
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys("13555944129")
        #滚动到保存按钮，然后点击保存
        # self.swipeDown(1000)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()




