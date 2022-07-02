from time import sleep

from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        #复用浏览器，需要先关闭已有的浏览器
        # assert self.main.goto_add_memeber().add_member()
        add_memeber = self.main.goto_add_memeber()
        add_memeber.add_member()
        sleep(5)
        assert add_memeber.get_memeber('aa_aa36')