from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_member.page.base_page import Base


class Contact(Base):
    def add_memeber(self):
        #点击添加成员按钮，通过css定位，找到三个元素，但是第0个元素没有显示，所以必须选择第1个或第2个元素
        self.find(By.CSS_SELECTOR, '.js_add_member:nth-child(2)').click()
        #input name:
        self.find(By.ID, 'username').send_keys("aa_aa37")
        #input uni id:
        self.find(By.ID, 'memberAdd_acctid').send_keys("aa_aa37")
        #cell phone number
        self.find(By.ID, 'memberAdd_phone').send_keys("13555944100")
        #click save button
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def page_update(self):
        #对页码1/10进行提取和分割出当前页和最后一页， 返回一个列表
        # content:str = self._driver.find_element(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        #.js_title>th>input
        WebDriverWait(self._dirver, 10).until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR, '.js_title>th>input'))
        content:str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        # split("/", 1)使用/作为分割符，进行1次切割
        return [int(x) for x in content.split('/', 1)]

    def get_member(self, value):
        '''
        :param value:
        :return:
        :description:
          #先获取页面上所有成员的姓名，放在列表里
        #'#member_list>tr>td:nth-child(2)'
        #对于多个页面的情况下，需要进行翻页，逐个页面进行获取成员姓名
        #获取页码信息：
        '''
        cur_page, total_page = self.page_update()
        while True:
            memebers = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

            for memeber in memebers:
                if value ==  memeber.get_attribute("title"):
                    return True

            cur_page = self.page_update()[0]
            if cur_page == total_page:
                return False

            self.find(By.CSS_SELECTOR, ".js_next_page").click()






