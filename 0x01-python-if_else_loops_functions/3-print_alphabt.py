#!/usr/bin/python3
for alphabet in range(ord("a"), ord("z")+1):
    if alphabet == 101 or alphabet == 113:
        pass
    else:
        print("{:c}".format(alphabet), end="")
