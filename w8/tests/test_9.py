import itertools
import pytest

def maximize(lists, m):
    squared_maxes = [max(lst)**2 for lst in lists]
    polynomials = [p for p in itertools.accumulate(squared_maxes)]
    return max([x % m for x in polynomials])


@pytest.mark.parametrize("lists,m", [([[5, 4],[7, 8, 9],[5, 7, 8, 9, 10]],1000), ([[1, 2, 3],[4, 5, 6],[1,10]],100), ([[10, 100],[5,5,5,5],[3,7,9]],10)])
def test_maximize(lists,m):
    assert maximize(lists, m) == max([x % m for x in [p for p in itertools.accumulate([max(lst)**2 for lst in lists])]])
