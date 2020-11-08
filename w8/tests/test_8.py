import itertools

def compress_string(s):
    groups = []
    uniquekeys = []
    for k, g in itertools.groupby(s):
        groups.append(len(list(g)))
        uniquekeys.append(int(k))
    return list(zip(groups, uniquekeys))


def test_compress_string():
    assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]
    assert compress_string('1234567890') == [(1, 1), (1, 2), (1, 3), (1, 4),
                                             (1, 5), (1, 6), (1, 7), (1, 8),
                                             (1, 9), (1, 0)]
    assert compress_string('123123123123123123') == [(1, 1), (1, 2), (1, 3),
                                                     (1, 1), (1, 2), (1, 3),
                                                     (1, 1), (1, 2), (1, 3),
                                                     (1, 1), (1, 2), (1, 3),
                                                     (1, 1), (1, 2), (1, 3),
                                                     (1, 1), (1, 2), (1, 3)]
