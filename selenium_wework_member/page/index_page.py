from selenium.webdriver.common.by import By

from selenium_wework_member.page.base_page import Base
from selenium_wework_member.page.contact_page import Contact


class IndexPO(Base):
    #点击菜单里的“通讯录”进入通信录页面
    #主要进入到通讯录页面需要返回这个页面
    def goto_contact(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return Contact(self)

