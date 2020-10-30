import pytest
from my_mathematics.vector import Vector

@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-4,-10,3],[2,14,6]),([0,0,0],[0,0,0])])
def test_add(v1,v2):
    np_ar1 = np.array(v1)
    np_ar2 = np.array(v2)
    vect1 = Vector(','.join(map(str,v1)))
    vect2 = Vector(','.join(map(str,v2)))
    a = str(np_ar1+np_ar2)
    a = list(a[1:-1].split(' '))
    a = list(i for i in a if i!='')
    assert str(vect1+vect2) == ','.join(a)


@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-4,-10,3],[2,14,6]),([0,0,0],[0,0,0])])
def test_sub(v1,v2):
    np_ar1 = np.array(v1)
    np_ar2 = np.array(v2)
    vect1 = Vector(','.join(map(str,v1)))
    vect2 = Vector(','.join(map(str,v2)))
    a = str(np_ar1-np_ar2)
    a = list(a[1:-1].split(' '))
    a = list(i for i in a if i!='')
    assert str(vect1-vect2) == ','.join(a)

@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-4,-10,3],[2,14,6]),([0,0,0],[0,0,0])])
def test_mul(v1,v2):
    np_ar1 = np.array(v1)
    np_ar2 = np.array(v2)
    vect1 = Vector(','.join(map(str,v1)))
    vect2 = Vector(','.join(map(str,v2)))
    assert vect1*vect2 == np.sum(np_ar1*np_ar2)

@pytest.mark.parametrize("v1,v2",[([1,2,3],[3,4,5]),([-4,-10,3],[2,14,6]),([0,0,0],[0,0,0])])
def test_and(v1,v2):
    np_ar1 = np.array(v1)
    np_ar2 = np.array(v2)
    vect1 = Vector(','.join(map(str,v1)))
    vect2 = Vector(','.join(map(str,v2)))
    a = str(np.cross(np_ar1,np_ar2))
    a = list(a[1:-1].split(' '))
    a = list(i for i in a if i!='')
    assert str(vect1&vect2) == ','.join(a)
