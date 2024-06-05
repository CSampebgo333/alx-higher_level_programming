#!/usr/bin/python3
import sys


def main():
    number = sys.argv[1:]
    length_number = len(number)
    sum_number = 0
    if length_number > 1:
        for n in range(length_number):
            sum_number += int(number[n])
    elif length_number == 1:
        sum_number += int(number[0])
    elif length_number == 0:
        sum_number += 0
    else:
        pass
    print(sum_number)


if __name__ == "__main__":
    main()
