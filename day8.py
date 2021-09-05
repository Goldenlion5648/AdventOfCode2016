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
        _, b = line.split(" ")
        l, w = map(int, b.split("x"))
        print(l, w)
        for i in range(l):
            for j in range(w):
                board[(j, i)] = True
    elif "row" in line:
        cur = line.split(" ")
        y = int(cur[2][2:])
        amount = int(cur[-1])
        print("amount", amount)
        temp = board[(0, y)]
        temp_board = board.copy()
        for i in range(wide):
            board[(y, (i+amount) % wide)] = temp_board[(y, i)]
    elif "column" in line:
        cur = line.split(" ")
        x = int(cur[2][2:])
        amount = int(cur[-1])
        print("amount", amount)
        temp = board[(0, x)]
        temp_board = board.copy()
        for i in range(tall):
            board[((i+amount) % tall, x)] = temp_board[(i, x)]
        # board[((i - temp) % tall, x)] = temp
print(board)
show_board(board)
ans(sum(board.values()))

