import sys
import argparse


def fibonacci(n):
    n = int(n)
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', nargs='?')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print (fibonacci(namespace.n))


#
# print(fibonacci(n))
