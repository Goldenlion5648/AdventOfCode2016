from AoCLibrary import *

#part 1 done in 22:18
#part 2 done in 41:00
start = "pgflpeqp"

open_ = {"b", "c", "d", "e", "f"}
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dirs = {
    (-1, 0) : "U", (1, 0) :"D", (0, -1): "L", (0, 1) : "R"
}
fringe = deque([("", 0, 0)])
seen = dd(lambda : -1)
shortest = float("+inf")
while len(fringe) > 0:
    path, y, x = fringe.popleft()
    cur_hash = get_hash(start + path)[:4]
    if len(path) < seen[(y, x)]:
        continue
    seen[(y, x)] = max(seen[(y, x)], len(path))

    if (y, x) == (3,3):
        if seen[(y, x)] < shortest:
            #part 1
            ans(path, should_exit=False)
        shortest = min(shortest, seen[(y, x)])
        continue

    options = [i in open_ for i in cur_hash]
    for i, avail in enumerate(options):
        if not avail:
            continue
        dy, dx = moves[i]
        cur = (path+dirs[moves[i]], y+dy, x+dx)
        if 0 <= dy + y <= 3 and 0 <= dx + x <= 3:
            fringe.append(cur)

ans(seen[(3, 3)])

