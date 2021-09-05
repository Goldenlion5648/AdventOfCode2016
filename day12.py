from itertools import *
from collections import *
from math import *
import re
from AoCLibrary import *
with open("input12.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 done in 15:13
#part 2 done in 16:02
def run_computer(instructs, part2=False):
    pos = 0
    regs = defaultdict(int)
    if part2:
        regs['c'] = 1
    while pos < len(instructs):
        line = a[pos]
        cur = line.split(" ")

        ip = cur[0]
        if ip == "cpy":
            x = cur[1]
            y = cur[2]
            if x.isnumeric():
                regs[y] = int(x)
            else:
                regs[y] = int(regs[x])
        elif ip == "inc":
            regs[cur[1]] += 1
        elif ip == "dec":
            regs[cur[1]] -= 1
        elif ip == "jnz":
            x = cur[1]
            y = cur[2]
            if x.isnumeric():
                if int(x) != 0:
                    pos += int(y)
                    continue
            else:
                if (regs[x]) != 0:
                    pos += int(y)
                    continue
        else:
            assert False
        pos += 1

    ans(regs['a'], should_exit=False)

if __name__ == '__main__':
    run_computer(a)
    run_computer(a, part2=True)
318077
