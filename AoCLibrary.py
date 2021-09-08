import re
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
import os
import sys
from itertools import *
from math import *
from collections import defaultdict as dd
from collections import *
from copy import deepcopy
import hashlib

using_pypy = False
try:
    import pyperclip
except ModuleNotFoundError:
    using_pypy = True


def nums(a : str, negs=True):
    '''Returns a list with all the numbers from a string'''
    pattern = r"-?\d+" if negs else r"\d+"
    return [int(n) for n in re.findall(pattern, a.strip())]

# def num_ranges(a):
#     '''Returns a list with the numbers from a string'''
#     if type(a) == str:
#         a = a.strip().split('\n')
#     return [[int(num) for num in re.findall(r"\d+", x)]
#             for x in a]


def num_list(a, negs=True):
    '''Returns a list of lists with only the numbers
     from each line of a string or a list'''
    pattern = r"-?\d+" if negs else r"\d+"
    if type(a) == str:
        a = a.strip().split('\n')
    return [[int(num) for num in re.findall(pattern, x)] for x in a]

def prod(x):
    res = 1
    for i in x:
        res *= i
    return res

#aliases
num_lists = num_list
nums_lists = num_list
nums_list = num_list
nums2 = num_list

def p(*args):
    '''Faster way to type print'''
    print(*args)
def pprint(a):
    '''Takes a 2d list and prints in a nice way'''
    for y in a:
        print("".join(list(map(str, y))))

def get_hash(s):
    return hashlib.md5((s).encode('utf-8')).hexdigest()

def read_board(a, start_regex_raw, goal_regex_raw, wall_regex=r"#"):
    board = {}
    goals = set()
    for y in range(len(a)):
        for x in range(len(a[0])):
            board[(y, x)] = bool(re.match(wall_regex, a[y][x]))
            if re.match(start_regex_raw, a[y][x]):
                startX = x
                startY = y
            if re.match(goal_regex_raw, a[y][x]):
                goals.add((y, x))
    return board, startY, startX, goals

def show_board(board, actual_symbol=False):
    '''Prints a defaultdict that uses (y, x) values for keys
    
    True  means # (wall) 

    False means . (open) 

    (isWall)
    '''
    y_dim = max(board, key=lambda x : x[0])[0] + 1
    x_dim = max(board, key=lambda x : x[1])[1] + 1
    for y in range(y_dim):
        for x in range(x_dim):
            if actual_symbol:
                print(board[(y, x)] if (y, x) in board else "_", end='')

            if (board[(y, x)]):
                print("#", end='')
            else:
                print(".", end='')
        print()


def bfs(startY, startX, goalY, goalX, board, max_steps=float("+inf")):
    '''Returns steps from start to goal, and seen (dict of (posY, posX) : steps away)
    
    given starting x and y, and goalX and goalY, and 
    dictionary of (y, x) as keys and bool values (True for # wall,
    False for . open)'''
    fringe = deque([(startY, startX, 0)])
    seen = dd(lambda: float("+inf"))
    seen[(startY, startX)] = 0
    yDim = max(j[0] for j in board.keys()) + 1
    xDim = max(j[1] for j in board.keys()) + 1
    def add_spot(newY, newX, steps):
        pot = (newY, newX)
        if 0 <= newY < yDim and 0 <= newX < xDim and not board[pot] and steps + 1 < seen[pot]:
            fringe.append((newY, newX, steps + 1))
            seen[pot] = steps + 1
    while fringe:
        y, x, steps = fringe.popleft()
        if steps >= max_steps:
            continue
        if (y, x) == (goalY, goalX):
            # ans(steps)
            return steps, seen
        for dy, dx in [(-1, 0), (1, 0), (0,1), (0, -1)]:
            add_spot(y + dy, x + dx, steps)
        # add_spot(y - 1, x, steps)
        # add_spot(y, x + 1, steps)
        # add_spot(y, x - 1, steps)

    return steps, seen

def ans(x, sep="", should_exit=True):
    '''copies an answer to the clipboard'''
    answer = sep.join(list(map(str,x))) if type(x) == list else str(x)
    if using_pypy:
        # print("COPY THIS TO THE CLIPBOARD!!!!")
        os.system(f"echo {answer} | clip.exe")
    else:
        pyperclip.copy(answer)
    print("copied to clipboard:")
    print(answer)
    if should_exit:
        exit()


# sourcery skip: de-morgan
directions = {
    "N" : (-1, 0),
    "S" : (1, 0),
    "E" : (0, 1),
    "W" : (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
adj8 = [(i, j) for i in range(-1, 2) 
                for j in range(-1, 2) 
                if not (i == 0 and j == 0)]
#aliases
ajd = adj
cardinals = adj
ajd8 = adj8
all_touching = adj8
