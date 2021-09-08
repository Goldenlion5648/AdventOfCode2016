from AoCLibrary import *

with open("input6.txt") as f:
    a = f.read().strip().split("\n")
    
#part 1 done in about 4-5 minutes
#part 2 done in 1:23 (around 6 minute mark)
def solve(part2=False):
    answer = []
    for i in range(len(a[0])):
        c = Counter()
        for line in a:
            c[line[i]] += 1
        if part2:
            answer.append(c.most_common()[-1][0])
        else:
            answer.append(c.most_common()[0][0])
    ans(answer, should_exit=False)

solve()
solve(True)
