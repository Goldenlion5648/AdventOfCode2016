from AoCLibrary import *

with open("input21.txt") as f:
    a = f.read().strip().split("\n")


def scramble(letters):
    if type(letters) == str:
        letters = list(letters)
    for line in a:
        cur = line.split()
        nums_ = nums(line)
        if len(nums_) >= 1:
            x = nums_[0]
        if len(nums_) >= 2:
            y = nums_[1]
        
        if cur[0] == 'swap':
            if nums_:
                letters[y], letters[x] = letters[x], letters[y]
            else:
                letters = list(("".join(letters)).replace(
                    cur[2], '_').replace(cur[-1], cur[2]).replace('_', cur[-1]))
        elif cur[0] == 'rotate':
            if cur[-2] == 'letter':
                index = letters.index(cur[-1])
                if index >= 4:
                    index += 1
                index += 1
            letters = deque(list(letters))
            if cur[1] == 'right':
                letters.rotate(x)
            elif cur[1] == 'left':
                letters.rotate(-x)
            else:
                letters.rotate(index)
            
            letters = list("".join(list(letters)))
        elif cur[0] == 'reverse':
            temp = letters[x:y + 1]
            letters[x:y + 1] = temp[::-1] 
        elif cur[0] == "move":
            temp = letters[x]
            letters.pop(x)
            letters.insert(y, temp)

    return "".join(letters)

ans(scramble("abcdefgh"), should_exit=False)

key = "fbgdceah"
#brute force instead of reversing instructions
for perm in permutations(list(key), 8):
    cur = scramble(list(perm))
    if cur == key:
        ans("".join(perm))
