import pytest
import itertools

def get_permutations(s, n):
    return sorted([''.join(x) for x in itertools.permutations(s, n)])


@pytest.mark.parametrize("s,n", [(['print'],(1)), (['lesson'],(2)), (['home'],(3))])
def test_permutations(s, n):
    assert get_permutations(s, n) == sorted([''.join(x) for x in itertools.permutations(s, n)])
