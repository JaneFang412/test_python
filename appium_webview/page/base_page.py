import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    logging.basicConfig(level=logging.INFO)
    #toast list,弹框列表
    _back_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),

    ]
    _max_num = 3
    _error_num = 0
    #初始化driver
    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    #封装self.driver.find_element()方法，并处理一些过程中遇到的弹框toast
    def find(self, locator, value:str=None):
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
                elelist = self._driver.find_elements(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    #自身调用自身，所有有可能出现死循环，需要设置循环次数
                    return self.find(locator, value)
            raise e

    def find_get_text(self, locator, value:str=None):
        element:WebElement
        try:
            if isinstance(locator, tuple):
                element_text = self._driver.find_element(*locator).text
            else:
                element_text = self._driver.find_element(locator, value).text
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element_text
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1

            for ele in self._back_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    #自身调用自身，所有有可能出现死循环，需要设置循环次数
                    return self.find_get_text(locator, value)
            raise e



