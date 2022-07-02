import pytest

@pytest.fixture()
def login():
    print("this is Login Method")

def pytest_configure(config):
    marker_list = ["search", "login"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )