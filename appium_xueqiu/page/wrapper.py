import logging
from selenium.webdriver.common.by import By
#处理弹窗
def handle_black(func):
    def wrapper(*args, **kwargs):
        from appium_xueqiu.page.basepage import BasePage
        # 各种可能弹框列表toast
        _back_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        # 最大循环次数
        _max_num = 3
        _error_num = 0
        instance:BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _back_list:
                logging.info(ele)
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # find方法自己调用自己，需要避免死循环，在这里要指定循环次数
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper




