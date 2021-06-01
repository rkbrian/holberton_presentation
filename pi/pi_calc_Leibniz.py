#!/usr/bin/python3

import sys

a = int(sys.argv[1])
n = 0
j = -1
if len(sys.argv) != 2:
    print("Error: please provide a valid number\n")
for i in range(a):
    j = j * (-1)
    n = n + (4 * j / (2 * i + 1))
print("Leibniz series")
print("My pi approximation after sum of {} fractions is\n{:.15f}".format(a, n))
print("Is my result anywhere close to the real pi value?\n3.141592653589793....")
