from AoCLibrary import *

with open("input13.txt") as f:
    num = int(f.read().strip())
# part 1 done in about 16 minutes
# part 2 done in about 20 minutes (off by 1 error, then doubt)
# num = 10
xDim = 60
yDim = 60
goalX, goalY = 31, 39
# goalX, goalY = 7, 4
board = defaultdict(str)
for y in range(yDim):
    for x in range(xDim):
        val = x*x + 3*x + 2*x*y + y + y*y
        val += num
        b = bin(val)[2:]
        c = b.count('1')
        board[(y, x)] = c % 2 == 1

# show_board(board)

ans(bfs(1, 1, goalY, goalX, board)[0], should_exit=False)
ans(len(bfs(1, 1, goalY, goalX, board, 50)[1]))
