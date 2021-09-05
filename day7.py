from AoCLibrary import *

with open("input7.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 in 43:20 (multiple brackets in one line forced regex :sigh:
#part 2 in 56:20

def part1():
    c = 0
    for line in a:
        works = True
        for brack in re.findall(r"(?<=\[).+?(?=\])", line):
            h=  brack
            # print(h)
            works = works and not any(
                h[x] == h[x+3] and h[x+1] == h[x+2] and
                h[x] != h[x+2] for x in range(len(h) - 3)
            )
        if not works:
            continue
        works = False
        for j in re.findall(r"((^|\]).+?(\[|$))", line):
            # print(j)
            for k in j:
                left = k.replace("[", "").replace("]", "")
                if len(left) < 4:
                    continue
                # p(left)
                works = works or \
                any(left[x] == left[x+3] and 
                    left[x+1] == left[x+2] and
                    left[x] != left[x+2] 
                    for x in range(len(left) - 3)
                    )

        c += works
    ans(c, should_exit=False)


def part2():
    c = 0
    for line in a:
        works = True
        pot = []
        for brack in re.findall(r"\[.+?\]", line):
            h = brack[1:-1]
            # print(h)
            for x in range(len(h) - 2):
                if (h[x] == h[x+2] and h[x] != h[x+1]):
                    pot.append((h[x], h[x+1]))
        # print(pot)
        works = False
        for j in re.findall(r"((^|\]).+?(\[|$))", line):
            # print(j)
            for k in j: 
                left = k.replace("[", "").replace("]", "")
                if len(left) < 3:
                    continue
                # p("left", left)
                for aa, bb in pot:
                    # print(aa, bb)
                    works = works or any(left[x] == bb and left[x + 2] == bb and left[x + 1] == aa for x in range(len(left) - 2)
                    )


        c += works
    ans(c)    

part1()
part2()
