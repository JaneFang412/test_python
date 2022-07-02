from appium_xueqiu2.page.app_page import App


class TestSearch():
    def setup(self):
        self.ser = App().start().main().goto_market().goto_search()

    def test_search(self):
        self.ser.search("BABA")
        assert self.ser.is_chosed("BABA")