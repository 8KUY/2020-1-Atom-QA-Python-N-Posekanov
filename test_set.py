import pytest

def test_copy(random_set):
    set = random_set
    set_copy = set.copy()
    assert set_copy == set

def test_pop(random_set):
    set = random_set
    l = len(set)
    set.pop()
    assert len(set) == l-1

def test_issubtest():
    set = {i for i in range(10)}
    other_set = {2,4,6}
    assert set.issuperset(other_set)

class TestNegative:
    def test_discard(self):
        set = {i for i in range(10)}
        set.discard(5)
        with pytest.raises(AssertionError):
            assert set.issuperset({5})

    def test_remove(self):
        set = {i for i in range(10)}
        with pytest.raises(KeyError):
            assert set.remove(20)
