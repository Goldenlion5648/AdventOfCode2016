from AoCLibrary import *

with open("input18.txt") as f:
    board = [list(f.read().strip())]

#part 1 done in 16:30 (wrong answer due to sample number of rows instead of real)
#part 2 done in 16:56
'''
Trap if:
Its left and center tiles are traps, but its right tile is not.
Its center and right tiles are traps, but its left tile is not.
Only its left tile is a trap.
Only its right tile is a trap.
In any other situation, the new tile is safe'''
# board = a
trap_mark = '^'
def is_trap(left, center, right):
    trap = False
    if not left and not center and right:
        trap = True
    if not center and not right and left:
        trap = True
    if center and right and not left:
        trap = True
    if center and not right and left:
        trap = True
    return trap

def find_traps(board, rows):  # sourcery skip: simplify-numeric-comparison
    # board = deepcopy(og)
    for y in range(1, rows):
        board.append(list('.'*len(board[0])))
        for x in range(len(board[0])):
            left = (x - 1 < 0 or board[y-1][x-1] != trap_mark)
            center = (board[y-1][x] != trap_mark)
            right = (x + 1 >= len(board[0]) or board[y-1][x+1] != trap_mark)
            if is_trap(left, center, right):
                board[y][x] = trap_mark
    # pprint(board)
    ans(sum(j.count(".") for j in board), should_exit=False)
    
find_traps(board[:], 40)
find_traps(board[:], 400000)
