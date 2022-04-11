import pytest

@pytest.fixture(autouse=True)
def open():
    print("Open browser")

def test_search2():
    print("test_search2")
    pass

def test_search3():
    print("test_search3")
    pass
if __name__ == '__main__':
    pytest.main()