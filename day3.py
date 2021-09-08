from AoCLibrary import *

with open("input3.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 in 3:03
#part 2 in 7:54

def part1(a):
    count = 0
    for line in a:
        cur = nums(line)
        cur.sort()
        a, b, c = cur
        count += a + b > c
    ans(count, should_exit=False)

def part2(a):
    count = 0
    first = []
    mid= []
    last= []
    for line in a:
        a, b, c = nums(line)
        first.append(a)
        mid.append(b)
        last.append(c)
    combined = deque(first + mid + last)
    count = 0 
    while len(combined) > 0:
        cur = [combined.popleft() for _ in range(3)]
        cur.sort()
        a, b, c = cur
        count += a + b > c
    ans(count, should_exit=False)

part1(a)
part2(a)
