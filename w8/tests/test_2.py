def fibgen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib(n):
    func = fibgen()
    end = []
    for _ in range(n):
        end.append(next(func))
    return end


def test_fib():
    assert fib(4) == [0, 1, 1, 2]
    assert fib(7) == [0, 1, 1, 2, 3, 5, 8]
    assert fib(9)[3] == 2
