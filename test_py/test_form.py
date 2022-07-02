from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.ID, 'user_login').send_keys("123")
        self.driver.find_element(By.ID, 'user_password').send_keys("password")
        # self.driver.find_element(By.ID, 'user_remember_me').click()
        self.driver.find_element(By.NAME, 'commit').click()
        sleep(5)
