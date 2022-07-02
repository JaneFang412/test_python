import pytest

class TestClass:

    @pytest.mark.slow
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def f(self):
        raise SystemExit(1)

    def test_mytest(self):
        with pytest.raises(SystemExit):
            f()
