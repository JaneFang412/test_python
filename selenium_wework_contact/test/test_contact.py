from selenium_wework_contact.page.home import Home


class TestContact:
    def setup(self):
        self.home = Home()

    def test_contact(self):
        addmember = self.home.goto_contact().goto_addmemeber()
        addmember.add_memeber()
        memebers = addmember.get_memebers()
        assert "abf" in memebers