from AoCLibrary import *

with open("input2.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
# print(a)
#part 1 in 13:02
#part 2 in 19:57

def part1():
    board = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    cur = (1,1)
    answer = [0]
    for line in a:
        for letter in line:
            # print(letter)
            y, x = directions[letter]
            cur = (cur[0] + y, cur[1] + x)
            cur = (max(cur[0], 0), max(cur[1], 0))
            cur = (min(cur[0], len(board)-1), min(cur[1], len(board[0])-1))
            # print(cur)
        pos = board[cur[0]][cur[1]]
        if answer[-1] != pos: 
            answer.append(pos)
        # print(answer)
    ans(answer[1:], should_exit=False)

def part2():
    BLK = "0"
    board = [[BLK, BLK, "1", BLK, BLK],
            [BLK, "2", "3", "4", BLK], 
            ["5", "6", "7", "8", "9"],
            [BLK, "A", "B", "C", BLK], 
            [BLK, BLK, "D", BLK, BLK]]
    cur = (2,0)
    answer = ["0"]
    for line in a:
        for x in line:
            # print(x)
            new_y = cur[0] + directions[x][0]
            new_x = cur[1] + directions[x][1]

            if 0 <= new_y < len(board) and \
            0 <= new_x < len(board[0]) and \
                board[new_y][new_x] != BLK:
                cur = (new_y, new_x)
        pos = board[cur[0]][cur[1]]
        if answer[-1] != pos:
            answer.append(pos)

    ans(answer[1:])

part1()
part2()
