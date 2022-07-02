from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    _driver = None
    _url_add = ""

    def __init__(self, driver:WebDriver=None):
        #在Base类的构造方法__init__中，设置浏览器
        #并且创建webdriver的实力，用这个实例去调用webdriver提供的各种方法
        if driver == None:
            #浏览器复用,需要在cmd窗口中执行命令chrome --remote-debugging-port=9222
            #会自动打开一个chrome浏览器，这个个模式是可调式模式，在这个打开的浏览器里运行
            #不需要每次执行case都重新打开一个流量器，提供自动化开发效率
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver

        if self._url_add != "":
            self._driver.get(self._url_add)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_tobe_clickable(self, locator):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))







