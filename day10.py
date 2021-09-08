from AoCLibrary import *

with open("input10.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 done in 12:34, would be 18th on leaderboard :O
#part 2 done in 15:14, would be 12th on leaderboard :O :D

a.sort(reverse=True)
bots = dd(list)
outputs = dd(list)
k1, k2 = 5, 2
k1, k2 = 61, 17
fringe = deque(a)
while len(fringe):
    line = fringe.popleft()
    cur = line.split(" ")
    if line.startswith("value"):
        x, y = nums(line)
        bots[y].append(x)
    elif line.startswith("bot"):
        bot_num, x, z = nums(line)
        bots[bot_num].sort()
        if k1 in bots[bot_num] and k2 in bots[bot_num]:
            ans(bot_num, should_exit=False)
        if len(bots[bot_num]) >= 2:
            lo, hi = bots[bot_num]
        else:
            fringe.append(line)
            continue
        
        if cur[5] == 'output':
            outputs[x].append(lo)
        else:
            bots[x].append(lo)
        if cur[-2] == 'output':
            outputs[z].append(hi)
        else:
            bots[z].append(hi)

ans(prod([outputs[i][0] for i in range(3)]))
