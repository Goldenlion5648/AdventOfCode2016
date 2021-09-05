from AoCLibrary import *

with open("input3.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 in 3:03
#part 2 in 7:54

def part1(a):
    count = 0
    for line in a:
        cur = list(map(int, line.strip().split()))
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
        cur = list(map(int, line.strip().split()))
        a, b, c = cur
        first.append(a)
        mid.append(b)
        last.append(c)
    all_ = deque(first + mid + last)
    count = 0 
    while len(all_) > 0:
        cur = [all_.popleft() for i in range(3)]
        cur.sort()
        a, b, c = cur
        count += a + b > c
    ans(count, should_exit=False)

part1(a)
part2(a)
