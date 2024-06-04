#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    number_argv = len(argv)
    if number_argv > 1:
        print("{:d} arguments:".format(number_argv))
        for n, args in enumerate(argv, start=1):
            print("{:d}: {}".format(n, args))
    elif number_argv == 1:
        print("{:d} argument:".format(number_argv))
        print("{:d}: {}".format(number_argv, argv[0]))
    elif number_argv == 0:
        print("{:d} arguments.".format(number_argv))
    else:
        pass


if __name__ == "__main__":
    main()
