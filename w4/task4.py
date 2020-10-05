import sys
import argparse
import math


def get_primes(n):
    lst = []
    candidate = 2
    while (len(lst) < n):
        nokey = 1
        for j in range(2, int(math.sqrt(candidate+1)+1)):
            if candidate%j == 0 and j != candidate:
                nokey = 0
                break
            else:
                pass
        if nokey:
            lst.append(candidate)
        candidate += 1
    return lst


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--show-all', action='store_true', default=False)
    parser.add_argument('-f', '--file', type=argparse.FileType('w', encoding='utf8'))
    parser.add_argument('number', type=int)
    return parser


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()

    prime = get_primes(args.number)[-1]
    out1 = "{}th prime number is {}".format(args.number, prime)
    print(out1)


    if args.file is not None:
        print(out1, file=args.file)

    if args.show_all:
        before = get_primes(prime)
        print(*before)
        if args.file is not None:
            print(*before, file=args.file)

    if args.file is not None:
        args.file.close()

    print()
