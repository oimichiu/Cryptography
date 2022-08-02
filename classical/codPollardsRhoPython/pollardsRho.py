from itertools import count
from math import gcd
import sys

# number, x = 206488, 2
number, x = 16814905693, 2

for cycle in count(1):
    y = x
    for i in range(2 ** cycle):
        x = (x * x + 1) % number
        factor = gcd(x - y, number)
        if factor > 1:
            print("Factorul numărului n = 16814905693 este", factor)
            sys.exit()