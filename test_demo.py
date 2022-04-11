import pytest
import yaml

class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("this is test environment")
            print(env)
        elif "dev" in env:
            print("this is dev environment")

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))
