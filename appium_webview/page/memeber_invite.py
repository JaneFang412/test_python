from appium.webdriver.common.mobileby import MobileBy

from appium_webview.page.base_page import BasePage


class MemeberInvite(BasePage):

    def addmemeber_by_manual(self):
        # 局部导入，因为这两个类是相互返回，所有需要局部导入，否则会报错
        from appium_webview.page.contact_add import ContactAdd
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        # return "toast"
