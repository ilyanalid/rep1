from multiprocessing import Pool


def scalar(c1,c2):
    return c1*c2


def scalar1(c):
    return c[0] * c[1]

if __name__ == "__main__":
    v1=[1,2,3]
    v2=[2,3,4]

    pool = Pool(processes=4)
    results1 = [pool.apply(scalar, args=(i, j)) for i, j in zip(v1, v2)]
    print(sum(results1))
    results = pool.map(scalar1, zip(v1, v2))
    print(sum(results))
