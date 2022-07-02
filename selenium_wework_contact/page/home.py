from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wework_contact.page.add_memebers import AddMembers
from selenium_wework_contact.page.contact import Contact


class Home():
    def __init__(self):
        #浏览器复用
        options = Options()
        options.debugger_address="127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        # self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_contact(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return Contact(self._driver)


