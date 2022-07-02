from appium_wework.page.app_page import App
from appium_wework.page.basepage import Base


class TestContact():

    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.stop()


    def test_addcontact(self):
        invtpage = self.main.click_address_list().click_add_memeber().\
            click_add_by_manual().input_name().choose_gender().\
            input_mail().input_phonenum().click_save()

        assert '成功' in invtpage.get_toast()

