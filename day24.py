from AoCLibrary import *

with open("input24.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
    # a = f.read().strip()

#part 1 done in 1:08:52
#part 1 done in 1:09:56

board, startY, startX, goals = read_board(a, r"0", r"[0-9]")

# print(startY, startX)
#pre calculate the distance from each number marker to each other one
cache = dd(dict)
for i in goals:
    for j in goals:
        if i == j:
            continue
        cur = bfs(*i, *j, board)
        # print(cur)
        cache[i][j] = cur[0]


#position of 0 marker
start_spot = (startY, startX)

def get_shortest_path(end=None):
    answer = float("+inf")
    for perm in permutations(goals - {start_spot}):
        path = [start_spot] + list(perm)
        if end is not None:
            path += [end]
        answer = min(answer, 
        sum(cache[path[i]][path[i+1]] for i in range(len(path)-1)))
    return answer

ans(get_shortest_path(), should_exit=False)
ans(get_shortest_path(end=start_spot))
