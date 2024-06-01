#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(10):
        if n1 != n2 and n1 < n2:
            combination = "{:d}{:d}".format(n1, n2)
            if combination != "89":
                print(combination, end=", ")
            else:
                print(combination)
