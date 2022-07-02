import pytest

def test_case1(login):
    print("test_case1")
    pass

def test_case2():
    print("test_case2")
    pass

def test_case3(login):
    print("test_case3")
    pass

if __name__ == '__main__':
    pytest.main()