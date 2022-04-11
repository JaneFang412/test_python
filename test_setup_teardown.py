import pytest

def setup_module():
    print("this is setup_module method")

def teardown_module():
    print("this is teardown_module method")

def setup_function():
    print("this is setup_function")

def teardown_function():
    print("this is teardown_function")

def test_login():
    print("login method")

class testDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def teardown_class(self):
        print("teardown_class")


if __name__=='__main__':
      pytest.main("-v -s")