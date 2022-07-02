from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
import pytest
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        element_doubleclick = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        element_rightclick = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        elem = self.driver.find_element(By.ID, 's-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(elem)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_elem = self.driver.find_element(By.ID, 'dragger')
        drop_elem = self.driver.find_element(By.XPATH,'/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_elem, drop_elem).perform()
        # action.click_and_hold(drag_elem).release(drop_elem).perform()
        action.click_and_hold(drag_elem).move_to_element(drop_elem).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        username = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        # password = self.driver.find_element(By.XPATH, '/html/body/label[2]/table/tbody/tr/td[2]/input')
        username.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

