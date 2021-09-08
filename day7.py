from AoCLibrary import *

with open("input7.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

#part 1 in 43:20 (multiple brackets in one line forced regex :sigh: )
#part 2 in 56:20

def count_matches(pattern, words):
    return sum(bool(re.search(pattern, "".join(word)))
    for word in words)

def part1():
    c = 0
    abba = r"(.)((?:(?!\1)).)(\2\1)"
    for line in a:
        split_up = re.split(r"\[|\]", line)
        works = count_matches(abba, split_up[1::2]) == 0
        works = works and count_matches(abba, split_up[::2]) > 0

        c += works
    ans(c, should_exit=False)


def part2():
    c = 0
    for line in a:
        works = True
        pot = []
        for brack in re.findall(r"\[.+?\]", line):
            h = brack[1:-1]
            for x in range(len(h) - 2):
                if (h[x] == h[x+2] and h[x] != h[x+1]):
                    #get letters to look for
                    pot.append((h[x], h[x+1]))
        works = False
        for j in re.findall(r"((^|\]).+?(\[|$))", line):
            for k in j: 
                left = k.replace("[", "").replace("]", "")
                if len(left) < 3:
                    continue
                for aa, bb in pot:
                    # print(aa, bb)
                    works = works or any(left[x] == bb and left[x + 2] == bb and left[x + 1] == aa for x in range(len(left) - 2)
                    )


        c += works
    ans(c)    

part1()
part2()
