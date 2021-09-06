from AoCLibrary import *

with open("input15.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 done in 18:54
#part 2 done in 20:01

disks = {}
def read_input(a):
    for line in a:
        cur = line.split(" ")
        #pos count, start
        tup = int(cur[3]), int(cur[-1].strip("."))
        disks[int(cur[1][1:])] = tup

def play():
    pos = 0
    while True:
        works = True
        for o in order:
            num = o[0]
            pos_count, start = o[1]
            if (pos + start + num) % pos_count != 0:
                works = False
                break
        if works:
            ans(pos, should_exit=False)
            break
        pos += 1

read_input(a)
order = disks.items()
play()
part2_extra = "Disc #7 has 11 positions; at time=0, it is at position 0."
read_input(a + [part2_extra])
order = disks.items()
play()

