from selenium_wework_member.page.index_page import IndexPO


class TestAdd():
    def setup(self):
        self.index = IndexPO()
        pass

    def test_add_memebers(self):
        #首页-》点击contact->添加成员
        self.index.goto_contact().add_memeber()

        #添加成员之后查看添加的成员
        memebers = self.index.goto_contact().get_member()
        assert 'aa' in memebers



