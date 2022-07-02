from selenium.webdriver.common.by import By

from appium_xueqiu2.page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        self.find(By.XPATH, f"//*[@text='{name}']/..//*[@text='阿里巴巴']").click()
        self.find(By.XPATH, f"//*[@text='{name}']/../../..//*[@text='加自选']").click()

    def is_chosed(self, name):
        #//*[@text='BABA']/../../..//*[@text='已添加']
        ele = self.finds(By.XPATH, f"//*[@text='{name}']/../../..//*[@text='已添加']")
        return len(ele)>0
