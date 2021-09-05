from AoCLibrary import *

from copy import deepcopy
with open("input11.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")

floors = defaultdict(set)

for line in a:
    cur = line.split(" ")
    k = cur[1]
    word = "contains"
    items = re.split(r" and |, ", line[line.index(word)+len(word):])
    res = [i.replace("and ", "").strip().replace("a ", "") for i in items]
    print(res)
    floors[k] = set(res)
print(floors) 
seen = set()
order = ["first",
         "second",
         "third",
         "fourth"]
floors[order[-1]].pop()
start = floors.copy()
def to_tup(d):
    # print("ret", ret)
    return tuple((k, tuple(sorted(v))) for k, v in d.items())
#state, current_floor, steps_taken
start = (to_tup(floors.copy()), 0, 0)
fringe = deque([start])
print(floors)
seen.add(to_tup(floors.copy()))
highest = -1
cutoff = .85
goals = defaultdict(int)
while len(fringe):
    # if len(fringe) % 2000 == 0:
    #     print("fringe len", len(fringe))
    cur, fn, steps = (fringe.popleft())
    cur = {k : set(v) for k, v in cur}
    score = sum((val) * (len(cur[z]) * 2) for val, z in enumerate(cur))
    # id_ = tuple([len(temp[z]) for z in temp])
    goals[steps] = max(goals[steps], score)
    if score <= goals[steps] * cutoff:
        continue

    if steps > highest:
        highest = steps
        print(highest)
    f = order[fn]
    abort = False
    options = cur[f].copy()
    if len(cur[order[-1]]) and all(len(cur[order[i]]) == 0 for i in range(3)):
        ans(steps)
    for n in [-1, 1]:
        if fn + n < 0 or fn + n > 3:
            # print("continued")
            continue
        for thing in options:
            choices2 = {None} if n == -1 else options
            for thing2 in choices2:
                if thing == thing2:
                    continue
                temp = deepcopy(cur)
                # print("things", thing, thing2)
                if thing in temp[f]:
                    temp[f].discard(thing)
                    temp[order[fn + n]].add(thing)
                else:
                    assert False
                if thing2 is None or thing2 in temp[f]:
                    temp[f].discard(thing2)
                    if thing2 is not None:
                        temp[order[fn + n]].add(thing2)
                else:
                    assert False
                # print("new temp is", temp)
                pot = to_tup(temp.copy())
                seen_pot = pot, fn + n
                if seen_pot in seen:
                    continue
                num = 1
                abort = False
                # print("order", order)
                # print(fn + n)
                # print(f)
                for flr in [order[fn + n], order[fn]]:
                    # if any(item for item in flr:
                    chips = [re.split(r"-| ", x)[0] for x in temp[flr] if "microchip" in x]
                    gens = {re.split(r"-| ", x)[0]
                            for x in temp[flr] if "generator" in x}
                    # if True:
                    #     print("floor num", num)
                    #     print("chips", chips)
                    #     print("gens", gens)
                    for c in chips:
                        if c not in gens and len(gens):
                            abort = True
                            # print("aborted")
                            break
                    num += 1
                    if abort:
                        break
                if not abort:
                    score = sum((val) * (len(temp[z]) * 2) for val, z in enumerate(temp))
                    # id_ = tuple([len(temp[z]) for z in temp])
                    goals[steps + 1] = max(goals[steps + 1], score)
                    # print("added to fringe")
                    # print(score)
                    if score >= goals[steps + 1] * cutoff:
                        seen.add(seen_pot)
                        fringe.append((pot, fn + n, steps + 1))


print(len(fringe))
print(cur)
