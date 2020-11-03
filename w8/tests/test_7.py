import pytest
import itertools

def get_combinations_with_r(s, n):
    return sorted([''.join(sorted(x)) for x in itertools.combinations_with_replacement(s, n)])


@pytest.mark.parametrize("s,n", [(['print'],(1)), (['lesson'],(2)), (['home'],(3))])
def test_combinations_with_r(s, n):
    assert get_combinations_with_r(s, n) == sorted([''.join(sorted(x)) for x in itertools.combinations_with_replacement(s, n)])
