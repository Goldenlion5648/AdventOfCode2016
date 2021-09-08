from AoCLibrary import *

from copy import deepcopy
with open("input11.txt") as f:
    a = f.read().strip().split("\n")

def to_tup(d):
    return tuple((k, tuple(sorted(v))) for k, v in d.items())

floors = defaultdict(set)
word = "contains"
for line in a:
    cur = line.split(" ")
    k = cur[1]
    items = re.split(r" and |, ", line[line.index(word)+len(word):])
    res = [i.replace("and ", "").strip().replace("a ", "") for i in items]
    # print(res)
    floors[k] = set(res)

# print(floors) 
order = ["first",
         "second",
         "third",
         "fourth"]
floors[order[-1]].pop()

seen = set()
#state, current_floor, steps_taken
start = (to_tup(floors), 0, 0)
fringe = deque([start])
seen.add(to_tup(floors))
highest = -1
cutoff = .85
goals = defaultdict(int)

while len(fringe):
    cur, fn, steps = (fringe.popleft())
    cur = {k : set(v) for k, v in cur}
    # print(cur)
    score = sum((val) * (len(cur[z]) * 2) for val, z in enumerate(cur))
    goals[steps] = max(goals[steps], score)
    if score <= goals[steps] * cutoff:
        continue

    if steps > highest:
        highest = steps
        print(highest)
    floor_word = order[fn]
    abort = False
    options = cur[floor_word].copy()
    if len(cur[order[-1]]) and all(len(cur[order[i]]) == 0 for i in range(3)):
        ans(steps)
    for n in [-1, 1]:
        if fn + n < 0 or fn + n > 3:
            continue
        for thing in options:
            choices2 = {None} if n == -1 else options
            for thing2 in choices2:
                if thing == thing2:
                    continue
                temp = deepcopy(cur)

                temp[floor_word].discard(thing)
                temp[order[fn + n]].add(thing)
                temp[floor_word].discard(thing2)
                #check for moving second item down a floor (bad)
                if thing2 is not None:
                    temp[order[fn + n]].add(thing2)

                pot = to_tup(temp)
                seen_pot = pot, fn + n
                if seen_pot in seen:
                    continue
                num = 1
                abort = False
                for flr in [order[fn + n], order[fn]]:
                    chips = [re.split(r"-| ", x)[0] for x in temp[flr] if "microchip" in x]
                    gens = {re.split(r"-| ", x)[0]
                            for x in temp[flr] if "generator" in x}
                    abort = len(gens) and any(chip not in gens for chip in chips)
                    num += 1
                    if abort:
                        break
                else:
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
