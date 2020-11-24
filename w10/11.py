from multiprocessing import Pool


def scalar(c1,c2):
    return c1*c2

if __name__ == "__main__":
    v1=[1,2,3]
    v2=[2,3,4]

    pool = Pool(processes=4)
    results = [pool.apply(scalar,args = (i,j)) for i,j in zip(v1,v2)]
    print(sum(results))
