import math
import my_mathematics.math as my
import pytest

@pytest.mark.parametrize('num', [(math.pi), (2), (4), (0)])
def test_sin(num):
    assert my.MyMath.sin(num) == math.sin(num)
