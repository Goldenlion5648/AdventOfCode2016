from AoCLibrary import *

with open("input20.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
    # a = f.read().strip()

#part 1 done in 29:53 (was not taking the max of hi and hi2 :( ))
#part 2 done in 31:56

blacklist = nums2(a, False)
blacklist.append([4294967294, 4294967295])
blacklist.sort()
pos = 0
while pos < len(blacklist) - 1:
    lo, hi = blacklist[pos]
    lo2, hi2 = blacklist[pos + 1]
    if hi + 1>= lo2:
        blacklist.pop(pos+1)
        blacklist[pos] = [lo, max(hi2, hi)]
    else:
        pos += 1

pot = blacklist[0][1] + 1
ans(pot, should_exit=False)

total = sum(
    blacklist[i + 1][0] - blacklist[i][1] - 1
    for i in range(len(blacklist) - 1)
)

ans(total)
