import pytest
import itertools

def get_combinations(s, n):
    a = sorted([''.join(sorted(x)) for i in range(1, n+1) for x in itertools.combinations(s, i)])
    a.sort(key=lambda x: len(x))
    return a


@pytest.mark.parametrize("s,n", [(['print'],(1)), (['lesson'],(2)), (['home'],(3))])
def test_permutations(s, n):
    assert get_combinations(s, n) == sorted([''.join(sorted(x)) for i in range(1, n+1) for x in itertools.combinations(s, i)])
