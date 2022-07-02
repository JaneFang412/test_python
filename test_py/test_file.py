from time import sleep

from selenium.webdriver.common.by import By

from test_py.Base import Base
from selenium import webdriver

class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID, 'stfile').send_keys("C:/Users/Administrator/Desktop/upload.PNG")
        sleep(5)
