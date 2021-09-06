from AoCLibrary import *

with open("input21.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")
    # a = f.read().strip()


letters = list("abcde")
letters = list("abcdefgh")
def scramble(letters):
    if type(letters) == str:
        letters = list(letters)
    for line in a:
        cur = line.split()
        nums_ = nums(line)
        if cur[0] == 'swap':
            if nums_:
                letters[nums_[1]], letters[nums_[0]
                                    ] = letters[nums_[0]], letters[nums_[1]]
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
                letters.rotate(nums_[0])
            elif cur[1] == 'left':
                letters.rotate(-nums_[0])
            else:
                letters.rotate(index)
            
            letters = list("".join(list(letters)))
        elif cur[0] == 'reverse':
            temp = letters[nums_[0]:nums_[1] + 1]
            letters[nums_[0]:nums_[1] + 1] = temp[::-1] 
        elif cur[0] == "move":
            temp = letters[nums_[0]]
            letters.pop(nums_[0])
            letters.insert(nums_[1], temp)
        # print(letters)

    return ("".join(letters))

ans(scramble("abcdefgh"), should_exit=False)

key = "fbgdceah"
for perm in permutations(list("fbgdceah"), 8):
    cur = scramble(list(perm))
    if cur == key:
        ans("".join(perm))
