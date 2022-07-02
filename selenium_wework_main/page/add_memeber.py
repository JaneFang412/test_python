from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        # sleep(5)
        locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.wait_for_click(locator)
        self.find(By.ID, 'username').send_keys("aa_aa37")
        self.find(By.ID, 'memberAdd_acctid').send_keys("aa_aa37")
        self.find(By.ID, 'memberAdd_phone').send_keys("11111111124")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def update_page(self):
        #获取页码，保存成str类型
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        #对页码（1/10）以’/‘进行一次分割,分出当前页和最后一页。
        return [int(x) for x in content.split('/', 1)]

    def get_memeber(self, value):
        #wait for a while显示等待，需要等到页面加载完毕
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        #获取页面中的页面，当前页和总页数
        cur_page, total_page = self.update_page()

        while True:
            #获取成员列表中姓名列
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            #通过for循环判断要找的value是否在列表中，
            for element in elements:
                #取出姓名列的title属性
                if value == element.get_attribute("title"):
                    return True
            #重新再获取页面的页码
            cur_page = self.update_page()[0]
            #判断当前页是否是最后一页，如果是则突出循环。
            if cur_page == total_page:
                return False
            #点击下一页
            self.find(By.CSS_SELECTOR, '.js_next_page').click()



