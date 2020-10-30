import cmath
import my_mathematics.math as my
import pytest

@pytest.mark.parametrize('num', [(3+4j), (2), (4), (0)])
def test_complex(num):
    assert my.MyComplexMath.sqrt(num) ==  (cmath.sqrt(num).real, cmath.sqrt(num).imag)
