import inspect
import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from appium_xueqiu.page.wrapper import handle_black


class BasePage():
    _params={}
    #日志
    logging.basicConfig(level=logging.INFO)

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)


    @handle_black
    def find(self, locator, value:str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        self._error_num = 0
        self._driver.implicitly_wait(10)
        return element

    @handle_black
    def finds(self, locator, value:str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements
    @handle_black
    def find_and_get_text(self, locator, value: str=None):
        element: WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        # change python object to string
        raw = json.dumps(steps)
        #${name} -> name: 12345
        #12345
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0




