from AoCLibrary import *

with open("input9.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    # a = f.read().strip().split("\n")
    a = f.read().strip()
#part 1 in 15:44

seen = dict()

def expand(a):
    left = 0
    total = 0
    while True:
        if all(j not in a for j in "()"):
            seen[a] = len(a)
            total += len(a)
            return total
        try:
            old = left
            left = a.index("(", left)
            total += left - old
            right = a.index(")", left + 1)
        except:
            return total
        amount, rep = map(int, a[left+1:right].split("x"))
        end = right + amount + 1
        capture = a[right + 1:end]
        if capture not in seen:
            seen[capture] = expand(capture)
        total += seen[capture] * rep
        # print(capture, "*", rep, total)
        # extra = capture * rep
        a = a[end:]
        # print(a)

def get_value(capture):
    if capture in seen:
        return seen[capture]
    seen[capture] = expand(capture)
    return seen[capture]
    

def part1(a):
    cur = 0
    while True:
        try:
            cur = a.index("(", cur)
            other = a.index(")", cur + 1)
        except:
            break
        x, rep = map(int, a[cur+1:other].split("x"))
        end = other+x + 1
        capture = a[other + 1:end]
        extra = capture * rep
        a = a[:cur] + extra + a[end:]
        cur += len(extra)
        # print(a)

    ans(len(a.strip()), should_exit=False)


part1(a)
seen[a] = get_value(a)
ans(seen[a])
