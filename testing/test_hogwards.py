import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("http://www.testerhome.com")
        # self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        time.sleep(5)

