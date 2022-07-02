from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from selenium_wework_member.page.base_page import Base


class MemberInvite(Base):
    #继承Base类的init方法
    # def __init__(self, driver:WebDriver):
    #     self._driver = driver

    #点击手动输入添加，进入contact_add_page
    def click_add_by_manual(self):
        from appium_wework.page.contact_add_page import ContactAdd
        # 本地引入，因为contact_add_page与memeber_invite_page是相互返回的，容易引起死循环，所以采用本地导入
        # 也就是在方法内部导入避免死循环
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text