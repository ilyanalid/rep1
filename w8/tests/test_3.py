import pytest

def zip1(*iterables):
    sent = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        res = []
        for it in iterators:
            elem = next(it, sent)
            if elem is sent:
                return
            res.append(elem)
        yield tuple(res)


@pytest.mark.parametrize("a,b",[(['A','B','C'],[1,2,3]),(['x','y','z'],[2,14,6]),(['0','0','0'],[0,0,0])])
def test_zip(a,b):
    for pair in zip(zip1(a, b), zip(a, b)):
        assert pair[0] == pair[1]


def map1(func, iterable):
    for i in iterable:
        yield func(i)


@pytest.mark.parametrize("func,it",[(int,['1','2','3','4','5']) ,(abs,[-1, 0,-10]) ])
def test_map(func,it):
    for pair in zip(list(map1(func,it)), list(map(func,it))):
        assert pair[0] == pair[1]


def enumerate1(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

@pytest.mark.parametrize("list1",[(['str1', 'str2', 'str3']), (['1', '2', '3', '4'])])
def test_enumerate(list1):
    for pair in zip(enumerate1(list1), enumerate(list1)):
        assert pair[0] == pair[1]
