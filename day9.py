from AoCLibrary import *

with open("input9.txt") as f:
    a = f.read().strip()

#part 1 in 15:44

seen = dict()

def expand(a):
    left = 0
    total = 0
    while True:
        if all(paren not in a for paren in "()"):
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
            # print("ran")
        total += seen[capture] * rep
        # print(capture, "*", rep, total)
        # extra = capture * rep
        a = a[end:]
        # print(a)

def get_value(capture):
    if capture not in seen:
        seen[capture] = expand(capture)
    return seen[capture]
    

def part1(a):
    opening = 0
    while True:
        try:
            opening = a.index("(", opening)
            closing = a.index(")", opening + 1)
        except:
            break
        count, repeat = map(int, a[opening+1:closing].split("x"))
        end = closing + count + 1
        capture = a[closing + 1:end]
        extra = capture * repeat
        a = a[:opening] + extra + a[end:]
        opening += len(extra)
        # print(a)

    ans(len(a.strip()), should_exit=False)

part1(a)
ans(get_value(a))
