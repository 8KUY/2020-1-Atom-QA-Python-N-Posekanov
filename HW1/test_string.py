import pytest

def test_addition(random_string):
    string = random_string
    assert string+string == string * 2

class Test_NonParametrised:
    def test_NegativeisAlpha(self):
        string = '12345'
        with pytest.raises(AssertionError):
            assert string.isalpha()

    def test_find(self):
        string = 'hello world'
        assert string.find('world') == 6

    def test_title(self):
        string = 'hello world'
        assert string.title() == 'Hello World'

    def test_capitalize(self):
        string = 'HELLO WORLD'
        assert string.capitalize() == 'Hello world'