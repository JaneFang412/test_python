import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Base():
    #日志
    logging.basicConfig(level=logging.INFO)
    #各种可能弹框列表toast
    _back_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    #最大循环次数
    _max_num = 3
    _error_num = 0

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self, locator, value:str = None):
        logging.info(locator)
        logging.info(value)
        element:WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)

            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._back_list:
                logging.info(ele)
                elelist = self._driver.find_element(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    #find方法自己调用自己，需要避免死循环，在这里要指定循环次数
                    return self._driver.find(locator, value)
            raise e


