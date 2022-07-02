from time import sleep

from selenium.webdriver.common.by import By

from appium_yaml.page.basepage import BasePage


class Main(BasePage):

    def goto_search(self):
        # self.find(By.ID, 'tv_search').click()
        sleep(10)
        self.steps("../page/mail.yaml")