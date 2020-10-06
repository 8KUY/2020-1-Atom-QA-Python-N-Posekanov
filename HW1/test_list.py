
def test_append(random_value, random_list):
    list = random_list
    l = len(list)
    list.append(random_value)
    assert len(list) == l+1

def test_pop(random_list):
    list = random_list
    l = len(list)
    list.pop(0)
    assert len(list) == l-1

def test_reverse():
    list = [1,2,3,4]
    list.reverse()
    assert list == [4,3,2,1]

def test_len():
    list = [1, 2, 3, 4]
    assert len(list) == 4

class Test_NonParametrised:
    def test_insert(self):
        list = [1,2,3,4]
        a = 5
        list.insert(1,a)
        assert list == [1,5,2,3,4]