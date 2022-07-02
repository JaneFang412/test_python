from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wework_login.register import Register

class Login:
    #变量driver的类型是WebDriver,定义类型后可以直接使用WebDriver提供的方法,就是贴标签
    def __init__(self, driver:WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        #click register
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self._driver)
