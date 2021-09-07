from AoCLibrary import *

with open("input23.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

def run_computer(a, start):
    pos = 0
    regs = defaultdict(int)
    # regs['a'] = 63000
    regs['a'] = start
    # if part2:
    #     regs['c'] = 1
    time_step = 0
    while 0 <= pos < len(a):
        time_step += 1

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
        #custom opcode to speed up execution
        elif ip == "add":
            x = cur[1]
            y = cur[2]
            regs[y] += regs[x]
        #custom opcode to speed up execution
        elif ip == "spec":
            # print("running special")
            x = cur[1]
            rep = regs['d'] - 1
            regs['a'] += regs['b'] * rep
            regs['d'] = 0
        elif ip == "jnz":
            x = cur[1]
            y = cur[2]

            if (x.isnumeric() and int(x) != 0
                or not x.isnumeric() and regs[x] != 0):
                try:
                    pos += int(y)
                except:
                    pos += regs[y]
                # if pos in [6, 8]:
                    # input("jumped to " + str(pos))
                continue
        elif ip == "tgl":
            x = cur[1]
            assert x.isalpha()
            q = pos+regs[x]
            if q < 0 or q >= len(a):
                pos += 1
                # print("trying to toggle outside")
                continue
            before = a[q]
            # print("looking at pos", q)
            # print("before instruct", before)
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
        else:
            assert False
        pos += 1

    ans(regs['a'], should_exit=False)


run_computer(a.copy(), 7)
run_computer(a.copy(), 12)
