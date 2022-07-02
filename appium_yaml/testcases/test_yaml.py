import pytest
import yaml

from appium_yaml.page.app import App


class TestYaml:
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./testdata.yaml")))
    def test_yaml(self, value1, value2):
        # self.app = App()
        # self.app.start().main().goto_search()
        print(value1)
        print(value2)

