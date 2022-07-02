from time import sleep

from selenium.webdriver.common.by import By
from test_py.Base import Base
from selenium import webdriver


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        #跳转到注册窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("username")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("13555944127")
        sleep(3)
        self.driver.switch_to_window(windows[0])

        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys("1355559999")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys("password")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        sleep(3)


