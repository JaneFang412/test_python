import pytest

def test_a():
    print("test_a")

class TestDemo():
    def test_one(self):
        print("Start to run test_one method")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("start to run test_two method")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("Start to run test_three method")
        a = 'hello'
        b = 'hello world'
        assert a in b

class TestDemo1():
    def test_four(self):
        print("Start to run test_four method")
        x = 'this'
        assert 'h' in x


if __name__== '__main__':
    # pytest.main("-v -x TestDemo")
    pytest.main("-v -s TestDemo::test_one")

