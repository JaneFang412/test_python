from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_wework.page.basepage import Base
from appium_wework.page.member_invite_page import MemberInvite
class AddressList(Base):
    #继承Base类的init方法
    # def __init__(self, driver:WebDriver):
    #     self._driver = driver
    #点击添加成员，进入member_invite_page
    def click_add_memeber(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemberInvite(self._driver)