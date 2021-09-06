from AoCLibrary import *

#part 1 in 17:38
#part 2 in 19:06
def gen_data(a):
    b = a[::-1].replace("0", "x").replace("1", "0").replace("x", "1")
    return a + "0" + b

def checksum(a):
    res = [a[i:i+2] for i in range(0, len(a), 2)]
    res = (["1" if j[0] == j[1] else "0" for j in res])
    res = "".join(res)
    if len(res) % 2 == 0:
        return checksum(res)
    return res

def work(a, len_):
    while len(a) < len_:
        a = gen_data(a)
    # print(a)
    a = a[:len_]
    return checksum(a)
assert checksum("110010110100") == "100"
assert work("10000", 20) == "01100"
assert gen_data("1") == "100"
assert gen_data("0") == "001"
assert gen_data("11111") == "11111000000"
assert gen_data("111100001010") == "1111000010100101011110000"
ans(work("11011110011011101", 272), should_exit=False)
ans(work("11011110011011101", 35651584))
