from AoCLibrary import *

with open("input25.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

def run_computer(a, start):
    pos = 0
    regs = defaultdict(int)
    regs['a'] = start
    time_step = 0
    trans = []
    # print("next" + "#"*100)
    while 0 <= pos < len(a):
        time_step += 1
        if len(trans):
            if ([0,1] * 20)[:len(trans)] != trans:
                break
            if len(trans) >= 8:
                ans(start)
        line = a[pos]
        # print(line)
        cur = line.split(" ")
        ip = cur[0]
        if ip == "cpy":
            x = cur[1]
            y = cur[2]
            if y.isnumeric():
                pos += 1
                print("skipped")
                continue
            try:
                regs[y] = int(x)
            except:
                regs[y] = int(regs[x])
        elif ip == "inc":
            if len(cur) >= 3:
                pos += 1
                continue
            if cur[1].isalpha():
                regs[cur[1]] += 1
        elif ip == "dec":
            if len(cur) >= 3:
                pos += 1
                continue
            if cur[1].isalpha():
                regs[cur[1]] -= 1
        elif ip == "out":
            x = cur[1]
            trans.append(regs[x])
        elif ip == "add":
            x = cur[1]
            y = cur[2]
            regs[y] += regs[x]
        elif ip == "set":
            x = cur[1]
            y = cur[2]
            regs[x] = int(y)
        elif ip == "spec":
            # print("running special")
            x = cur[1]
            rep = regs['c'] - 1
            regs['d'] += 182 * rep
            # regs['d'] -= 1
            regs['b'] = 0
            regs['c'] = 0
        elif ip == "jnz":
            x = cur[1]
            y = cur[2]
            if (x.isnumeric() and int(x) != 0
                    or not x.isnumeric() and regs[x] != 0):
                try:
                    pos += int(y)
                except:
                    pos += regs[y]
                continue

        elif ip == "tgl":
            x = cur[1]
            assert x.isalpha()
            q = pos+regs[x]
            if q < 0 or q >= len(a):
                pos += 1
                print("trying to toggle outside")
                continue
            before = a[q]

            print("looking at pos", q)
            print("before instruct", before)
            if before.count(" ") == 1:
                if "inc" in before:
                    a[q] = "dec" + a[q][3:]
                else:
                    a[q] = "inc" + a[q][3:]
            elif before.count(" ") == 2:
                if "jnz" in before:
                    a[q] = "cpy" + a[q][3:]
                else:
                    a[q] = "jnz" + a[q][3:]
            else:
                assert False
            print("new instruct", a[q])
            input()

            # input("pausing")
        else:
            assert False
        pos += 1


for w in range(1, 1000000000):
    run_computer(a, w)
