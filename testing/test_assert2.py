import pytest

# def exc(x):
#     if x==0:
#         raise ValueError("Value not 0 or None")
#     return 2/x
#
# def test_raises():
#     with pytest.raises(ValueError, match="Value not 0 or None"):
#         exc(0)
#     assert eval("1+2") == 3
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2
