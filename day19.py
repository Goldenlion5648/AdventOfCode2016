from AoCLibrary import *

presents = dd(lambda : 1) #ended up not being used?

#part 1 done in 20:59
#part 2 done in 24:37, still good enough for 58 on leaderboard(?)

def part1(count):
    """ 
    numberphile cheaty alt way
    """
    # ans(int(bin(count)[3:] + '1', 2), should_exit=False)
    # return

    circle = {i: (i + 1) % count for i in range(count)}
    pos = 0
    while len(circle) > 1:
        temp = circle[circle[pos]]
        circle.pop(circle[pos])
        circle[pos] = temp
        pos = circle[pos]

    ans(list(circle.keys())[0] + 1, should_exit=False)


def part2(count):
    circle = dd(lambda: [-1, -1])
    for i in range(count):
        circle[i][0] = (i + 1) % count
        circle[i][1] = (i - 1) % count
    # only the person getting removed matters, 
    # not who is taking from them
    pop_pos = count // 2
    while len(circle) > 1:
        left, right = circle.pop(pop_pos)
        pop_pos = circle[left][0] if len(circle) % 2 == 0 else left
        circle[left][1] = right
        circle[right][0] = left

    ans(list(circle.keys())[0] + 1)

part1(3012210)
part2(3012210)
