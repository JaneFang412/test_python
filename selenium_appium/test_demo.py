from appium import webdriver

#
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0'
# desired_caps['deviceName']='emulator-5554'
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.quit()
from selenium.webdriver.common.by import By

desire_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
   "noReset" : True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)
el1 = driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search')
el1.click()
el2 = driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text')
el2.send_keys("aibaba")
# el3 = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android')