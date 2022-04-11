import pytest
@pytest.fixture(params=[1,2,3,'linda'])
def test_data(request):
    return request.param

def test_one(test_data):
    print("\ntest data: %s" % test_data)

if __name__ == '__main__':
    pytest.main()
