from AoCLibrary import *

with open("input10.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 done in 12:34, would be 18th on leaderboard :O
#part 2 done in 15:14, would be 12th on leaderboard :O :D

a.sort(reverse=True)
bots = defaultdict(list)
outputs = defaultdict(list)
k1, k2 = 5, 2
k1, k2 = 61, 17
fringe = deque(a)
while len(fringe):
    line = fringe.popleft()
    cur = line.split(" ")
    if line.startswith("value"):
        x = int(cur[1])
        y = int(cur[-1])
        bots[y].append(x)
    else:
        num = int(cur[1])
        bots[num].sort()
        if k1 in bots[num] and k2 in bots[num]:
            ans(num, should_exit=False)
        try:
            lo, hi = bots[num]
        except:
            fringe.append(line)
            continue
        x = int(cur[6])
        z = int(cur[-1])
        if cur[5] == 'output':
            outputs[x].append(lo)
        else:
            bots[x].append(lo)
        if cur[-2] == 'output':
            outputs[z].append(hi)
        else:
            bots[z].append(hi)

ans(prod([outputs[i][0] for i in range(3)]))
