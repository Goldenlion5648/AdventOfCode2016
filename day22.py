from AoCLibrary import *

with open("input22.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
    # a = f.read().strip()
# nodes = dd(int)
class Node:
    def __init__(self, x, y, size, used, avail, _):
         self.x=x
         self.y=y
         self.size=size
         self.used=used
         self.avail=avail
         self.has_special = False
    def __str__(self):
        self.calc_avail()
        return f"{self.used}/{self.size}"
    def calc_avail(self):
        self.avail = self.size - self.used
    def take_data_from(self, other):
        self.calc_avail()
        other.calc_avail()
        assert other.used <= self.avail
        self.used += other.used
        self.calc_avail()
        other.used = 0
        other.calc_avail()
    def can_take_from(self, other):
        self.calc_avail()
        other.calc_avail()
        return self.size >= other.used 

def show_nodes(cur_y, cur_x, goalY, goalX, nodes):
    for y in range(yDim):
        for x in range(xDim):
            if y == goalY and x == goalX:
                print("g", end='')
            elif y == cur_y and x == cur_x:
                print("_", end='')
            else:
                print(".", end='')
        print()
    print()

    for y in range(yDim):
        for x in range(xDim):
            print(str(nodes[(y, x)]), end='\t')
        print()
    print()


def get_board_str(board):
    k = sorted(board.keys())
    return " ".join(str(board[(y, x)]) for y, x in k)



nodes = {}
highX = -1
for line in a[2:]:
    n= nums(line)
    # x, y = n[0], n[1]
    highX = max(highX, n[0])
    nodes[(n[1], n[0])] = (Node(*n))
    if n[-2] == 0:
        full = n[1], n[0]
    if n[-3] == 0:
        empty_y, empty_x = n[1], n[0]

goalX = highX
goalY = 0

pairs = 0
# part 1, calculate pairs, based on a node being able to 
# fit inside another one
for n1 in nodes.values():
    for n2 in nodes.values():
        if n1 == n2:
            continue
        if n1.used != 0 and n1.used <= n2.avail:
            pairs += 1

ans(pairs, should_exit=False)


############slide the tile########### 
yDim = max(list(nodes.keys()), key=lambda x: x[0])[0] + 1
xDim = max(list(nodes.keys()), key=lambda x: x[1])[1] + 1

start = (empty_y, empty_x, 0, goalY, goalX)
fringe = deque([start])

# show_nodes(goalY, goalX,nodes)
seen = dd(lambda : float("+inf"))
seen[(empty_y, empty_x, goalY, goalX)] = 0
highest_steps = -1
board = deepcopy(nodes)
while fringe:
    y, x, steps, goalY, goalX = fringe.popleft()
    if (goalY, goalX) == (0, 0):
        ans(steps)

    temp_goalX = goalX
    temp_goalY = goalY
    for dy, dx in adj:
        goalY = temp_goalY
        goalX = temp_goalX
        pot = (y + dy, x + dx)
        newY = pot[0]
        newX = pot[1]
        if 0 <= newY < yDim and 0 <= newX < xDim and \
        board[(y, x)].can_take_from(board[pot]):
            if pot == (goalY, goalX):
                goalY, goalX = y, x
            nempty_xt_spot = (*pot, goalY, goalX)
            if seen[nempty_xt_spot] <= steps + 1:
                continue
            seen[nempty_xt_spot] = steps + 1
            fringe.append((*pot, steps + 1, goalY, goalX))
