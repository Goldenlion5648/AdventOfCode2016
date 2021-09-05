from AoCLibrary import *


import hashlib
#USE PYTHON, NOT PYPY


door = "ugkcyxxp"
answer = []
part2 = dict()
i = 0
while True:
    cur = hashlib.md5((door + str(i)).encode('utf-8')).hexdigest()
    if cur.startswith("00000"):
        answer.append(cur[5])
        if cur[5].isnumeric() and int(cur[5]) not in part2:
            part2[int(cur[5])] = cur[6]
        print("added")
        print(answer)
        if len(answer) == 8:
            ans(answer, should_exit=False)
        p(part2)
        if all(x in part2 for x in range(0, 8)):
            ans([part2[x] for x in range(0, 8)])
    if i % 100000 == 0:
        print(i)
    i += 1
