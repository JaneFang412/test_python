from appium_webview.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    # def teardwon(self):
    #     self.app.stop()

    def test_addcontact(self):
       invitepage = self.main.goto_addresslist().add_memeber().\
           addmemeber_by_manual().input_name().set_gender().\
           input_mail().input_phonenum().click_save()

       assert '成功' in invitepage.get_toast()
