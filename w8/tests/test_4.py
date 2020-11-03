import itertools
import pytest


def get_cartesian_product(a, b):
    return list(itertools.product(a, b))


@pytest.mark.parametrize("a,b", [([1, 2, 3],[1, 1, 1]), ([1,2],[1,1]), ([4, 5, 9],[10, 3, 8])])
def test_product(a, b):
    assert get_cartesian_product(a,b) == list(itertools.product(a, b))
