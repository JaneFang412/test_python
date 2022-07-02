from appium import webdriver
from selenium.webdriver.common.by import By
import time

desird_caps={}
desird_caps['platformName']='Android'
desird_caps['platformVersion']='6.0'
desird_caps['deviceName']='127.0.0.1:7555'
desird_caps['appPackage']='com.xueqiu.android'
desird_caps['appActivity']='com.xueqiu.android.common.MainActivity'
desird_caps['noReset'] = 'true'
desird_caps['dontStopAppOnReset']='true'
desird_caps['skipDeviceInitialization'] = 'true'
#与sever建立连接
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desird_caps)
driver.implicitly_wait(10)

#com.xueqiu.android:id/tv_search
driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys("alibaba")
driver.find_element_by_accessibility_id()
#返回到上一个页面
driver.back()
driver.back()
#/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.
# LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.
# FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.
# FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]
time.sleep(3)
driver.quit()
