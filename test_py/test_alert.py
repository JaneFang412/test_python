from time import sleep

from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By

from test_py.Base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换到iframe里
        self.driver.switch_to.frame("iframeResult")
        #定位到拖拽对象
        drag = self.driver.find_element(By.ID, "draggable")
        #定位到对象释放处
        drop = self.driver.find_element(By.ID, "droppable")
        #可以使用ActionChains提供的拖拽方法
        action = ActionChains(self.driver)
        # action.click_and_hold(drag).move_to_element(drop).release().perform()
        action.drag_and_drop(drag, drop).perform()

        sleep(4)
        print("Click Aert to confirm")

        #切换到alter对象上进行操作
        #接受现有警告框
        self.driver.switch_to.alert.accept()
        #从iframe切换到原来窗口
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,"submitBTN").click()
        sleep(3)


