from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_wework.page.basepage import Base


class ContactAdd(Base):
    # 继承Base类的init方法
    # def __init__(self, driver:WebDriver):
    #     self._driver = driver
    #输入姓名
    def input_name(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(
            "appium_t1")
        return self

    #选择性别
    def choose_gender(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self._driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    #输入mail
    def input_mail(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="企业邮箱　"]/..//*[@class="android.widget.EditText"]').send_keys("appium_t1")
        return self
    #输入电话
    def input_phonenum(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys("13555944129")
        return self

    #点击保存
    def click_save(self):
        #本地引入，因为contact_add_page与memeber_invite_page是相互返回的，容易引起死循环，所以采用本地导入
        #也就是在方法内部导入避免死循环
        from appium_wework.page.member_invite_page import MemberInvite
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        return MemberInvite(self._driver)