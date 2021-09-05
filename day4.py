from AoCLibrary import *

with open("input4.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")


def part1():
    count = 0
    for line in a:
        left, right= line.split("[")
        right = list(right[:-1])
        id_ = int(left.split("-")[-1])
        split_up = left.split("-")[:-1]
        joined = "".join(split_up)
        counts = Counter(joined)
        sorted_ = sorted([(counts[i], i) for i in counts], reverse=True)

        pos = 0
        while pos +1 < len(sorted_):
            start = pos
            while pos + 1 < len(sorted_) and sorted_[pos][0] == sorted_[pos+1][0]:
                pos += 1
            sorted_[start:pos+1] = sorted(sorted_[start:pos+1])
            pos += 1
        # print(sorted_)
        letters = [x[1] for x in sorted_[:len(right)]]
        # p("right", right)
        if ((letters)) == right:
            count += id_
    ans(count, should_exit=False)
def part2():
    count = 0
    for line in a:
        left, right = line.split("[")

        right = list(right[:-1])
        id_ = int(left.split("-")[-1])
        left = "".join(left.split("-")[:-1])
        left = left.replace("-", "")
        answer = [lowercase[(list(
            lowercase).index(k) + (id_ % 26)) % len(lowercase)] for k in left]
        answer = ("".join(answer))
        if "north" in answer:
            ans(id_)
        split_up = left.split("-")[:-1]
        joined = "".join(split_up)

part1()
part2()
