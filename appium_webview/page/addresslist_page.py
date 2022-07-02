from appium.webdriver.common.mobileby import MobileBy

from appium_webview.page.base_page import BasePage
from appium_webview.page.memeber_invite import MemeberInvite


class AddressList(BasePage):

    def add_memeber(self):
        self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemeberInvite(self._driver)
