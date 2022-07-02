from selenium.webdriver.common.by import By




def handle_black(func):
    def wrapper(*args, **kwargs):
        from appium_xueqiu2.page.base_page import BasePage

        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _err_num = 0
        instance:BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _err_num = 0
            instance._driver.implicitly_wait(15)
            return element
        except Exception as e:
            instance._driver.implicitly_wait(1)
            if _err_num > _max_num:
                raise e
            _err_num += 1
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            return e

    return wrapper








