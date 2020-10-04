import pytest
import random


@pytest.fixture(scope='function')
def random_list():
    list = []
    for i in range(random.randint(1,10)):
        list.append(random.randint(1,1000))
    yield list

@pytest.fixture(scope='function')
def random_set():
    set = {random.randint(1,1000)}
    for i in range(random.randint(1, 9)):
        set.add(random.randint(1,1000))
    yield set

@pytest.fixture(scope='function')
def random_dict():
    dict = {i:random.randint(1,1000) for i in range(10)}
    yield dict

@pytest.fixture(scope='function')
def random_string():
    string = ''
    for i in range(10):
        string = string + str(random.randint(0,10))
    yield string