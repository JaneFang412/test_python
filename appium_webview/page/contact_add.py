from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appium_webview.page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        self.find(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys("appium_t1")
        return self

    def set_gender(self):
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_mail(self):
        self.find(MobileBy.XPATH,
                                 '//*[@text="企业邮箱　"]/..//*[@class="android.widget.EditText"]').send_keys("appium_t1")
        return self
    def input_phonenum(self):
        self.find(MobileBy.XPATH, '//*[@text="手机号"]').send_keys("13555944129")
        return self

    def click_save(self):
        from appium_webview.page.memeber_invite import MemeberInvite
        #局部导入，因为这两个类是相互返回，所有需要局部导入，否则会报错
        sleep(2)
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        return MemeberInvite(self._driver)