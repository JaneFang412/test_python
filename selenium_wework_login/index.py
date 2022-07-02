from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_login.login import Login
from selenium_wework_login.register import Register


class Index:
    def __init__(self):
        self._dirver = webdriver.Chrome()
        self._dirver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        #click login button
        self._dirver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._dirver)

    def goto_register(self):
        #click register button
        self._dirver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._dirver)