def test_popitem(random_dict):
    dict = random_dict
    a = (9, dict[9])
    assert dict.popitem() == a

def test_get(random_dict):
    dict = random_dict
    a = dict[5]
    assert dict.get(5) == a

def test_detNone(random_dict):
    dict = random_dict
    assert dict.get(100) == None

class Test_NoParametrising:
    def test_ask(self):
        dict = {'first': 1, 'second': 2}
        assert dict['first'] == 1

    def test_copy(self):
        dict = {'first': 1, 'second': 2}
        dict_other = dict.copy()
        assert dict == dict_other
