from AoCLibrary import *

with open("input15.txt") as f:
    a = f.read().strip().split("\n")

#part 1 done in 18:54
#part 2 done in 20:01

disks = {}
def read_input(a):
    for line in a:
        #pos count, start
        num, poses, _, start = nums(line) 
        tup = poses, start
        disks[num] = tup

def play(order):
    pos = 0
    while True:
        for o in order:
            num = o[0]
            pos_count, start = o[1]
            if (pos + start + num) % pos_count != 0:
                break
        else:
            ans(pos, should_exit=False)
            break
        pos += 1

read_input(a)
# print(disks)
play(disks.items())
part2_extra = "Disc #7 has 11 positions; at time=0, it is at position 0."
read_input(a + [part2_extra])
play(disks.items())

