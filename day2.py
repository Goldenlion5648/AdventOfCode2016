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
        for x in line:
            # print(x)
            cur = (cur[0] + directions[x][0], cur[1] + directions[x][1])
            cur = (max(cur[0], 0), max(cur[1], 0))
            cur = (min(cur[0], 2), min(cur[1], 2))
        pos = board[cur[0]][cur[1]]
        if answer[-1] != pos: 
            answer.append(pos)
        # print(answer)
    ans(answer[1:], should_exit=False)

def part2():
    board = [["0", "0", "1", "0", "0"],
            ["0", "2", "3", "4", "0"], 
            ["5", "6", "7", "8", "9"],
            ["0", "A", "B", "C", "0"], 
            ["0", "0", "D", "0", "0"]]
    cur = (2,0)
    answer = ["0"]
    for line in a:
        for x in line:
            # print(x)
            f = cur[0] + directions[x][0]
            s = cur[1] + directions[x][1]

            if 0 <= f < 5 and 0 <= s < 5 and board[f][s] != "0":
                cur = (f, s)
        pos = board[cur[0]][cur[1]]
        if answer[-1] != pos:
            answer.append(pos)
        # print(answer)
    # ans("".join(list(map(str, answer))))
    ans(answer[1:])

part1()
part2()
