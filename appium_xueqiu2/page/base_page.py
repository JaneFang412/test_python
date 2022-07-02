from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

'''
BasePage类是所有类的父类，其他的类要继承父类
'''

class BasePage():
    #为了使用appium.webdriver类提供的方法函数，需要创建一个实例对象self._driver
    #driver的初始值设置为None
    def __init__(self, driver:WebDriver=None):
        self._driver = driver

    #抽象出自动化测试的公共方法，比如在每个测试操作动作中都要先找到对象，然后在进行各种操作
    #所有可以把找到对象作为一个公共方法。
    '''
    @desciption: 通过某种定位方式找到元素
    @locator: 定位方式(By.Xpath, Id, name, css..)
    @value: 对象xpath, id, name, css的值
    @return：找到元素后返回
    '''
    def find(self,locator, value:str=None):
        element: WebElement
        if isinstance(locator, tuple):
            #*locator是定位方式和值合并成一个元组传递给函数，如("id", "ku")，*号表示两个参数分开传值
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        # 将错误数_error_num重置为0
        self._error_num = 0
        #设置隐式等待时间为10秒
        self._driver.implicitly_wait(10)
        return element

    def finds(self, locator, value:str=None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)

        return elements





