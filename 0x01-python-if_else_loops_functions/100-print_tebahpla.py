#!/usr/bin/python3
add_to_ascii_value = 25
for i in range(ord('a'), ord('z')+1):
    ascii_value = i + add_to_ascii_value
    if ascii_value % 2 == 0:
        print_value = ascii_value
    else:
        print_value = ascii_value - 32
    print("{:c}".format(print_value), end="")
    add_to_ascii_value -= 2
