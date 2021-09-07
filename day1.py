from AoCLibrary import *

with open("input1.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split(", ")

def part1():
    facing = 0
    x = 0
    y = 0
    for i in a:
        # print(i)
        d, n = i[0], i[1:]
        n = int(n)
        if d == "L":
            facing -= 1
        else:
            facing += 1
        facing %= 4
        if facing == 0:
            y -= n
        elif facing == 1:
            x += n
        elif facing == 2:
            y += n
        elif facing == 3:
            x -= n
        cur = (y, x)
    ans(abs(x) + abs(y), should_exit=False)

def part2():
    facing = 0
    x = 0
    y = 0
    seen = {(0, 0)}
    for i in a:
        d, n = i[0], i[1:]
        n = int(n)
        if d == "L":
            facing -= 1
        else:
            facing += 1
        facing %= 4
        for _ in range(n):
            if facing == 0:
                y -= 1
            elif facing == 1:
                x += 1
            elif facing == 2:
                y += 1
            elif facing == 3:
                x -= 1
            cur = (y, x)
            if cur in seen:
                ans(abs(x) + abs(y))
            seen.add(cur)

part1()
part2()
