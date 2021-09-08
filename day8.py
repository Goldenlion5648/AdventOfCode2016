from AoCLibrary import *

with open("input8.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
board = defaultdict(bool)
wide = 50
tall = 6
#part 1 done in 30 minutes
#part 2 done in 30:34 minutes

# def show_board(board):
#     w = max(x[1] for x in board) + 1
#     h = max(x[0] for x in board) + 1
#     for j in range(h):
#         for i in range(w):
#             if (board[(j, i)]):
#                 print("#", end='')
#             else:
#                 print(".", end='')
#         print()

for line in a:
    if line.startswith("rect"):
        l, w = nums(line)
        for i in range(l):
            for j in range(w):
                board[(j, i)] = True

    elif "row" in line:
        y, amount = nums(line)
        temp_board = board.copy()
        for i in range(wide):
            board[(y, (i+amount) % wide)] = temp_board[(y, i)]
    elif "column" in line:
        x, amount = nums(line)
        temp_board = board.copy()
        for i in range(tall):
            board[((i+amount) % tall, x)] = temp_board[(i, x)]
        # board[((i - temp) % tall, x)] = temp
# print(board)
ans(sum(board.values()), should_exit=False)
show_board(board)

