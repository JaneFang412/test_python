import pytest

@pytest.fixture(scope="module")
def open():
    print("Open the browser")
    yield
    print("run teardonw!")
    print("close browser")

def test_search1(open):
    print("test_search1")
    raise NameError
    pass
def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass
if __name__ == '__main__':
    pytest.main()