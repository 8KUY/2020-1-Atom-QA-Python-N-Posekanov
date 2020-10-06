import pytest

class Test_NonParametrised:
    def test_NegativeDivisionFloat(self):
        with pytest.raises(AssertionError):
                assert 20/3 == 6.66

    def test_convertToInreger(self):
        string = '123'
        assert int(string) == 123

    def test_OctAndHex(self):
        assert int(0xf) == int(0o17)

def test_minus(random_dict):
    dict = random_dict
    assert dict[0] - dict[1] < dict[0]

def test_zeroDivision():
    with pytest.raises(ZeroDivisionError):
        assert 1/0