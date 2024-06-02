#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')+1):
            val = "{:c}".format(ord(i)-32)
        else:
            val = "{:c}".format(ord(i))
        print(val, end="")
    print()
