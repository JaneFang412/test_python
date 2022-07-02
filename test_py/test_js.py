import time

import pytest
from selenium.webdriver.common.by import By
from test_py.Base import Base

class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,"kw").send_keys("test")
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, '下一页 >').click()
        time.sleep(5)
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        #或者
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_timedata(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script(
            'a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2022-04-16"')
        time.sleep(5)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
