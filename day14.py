from AoCLibrary import *

a = "abc"
a = "jlmsuwbz"
#num to hash
hash_storage = {}
#letter to numbers
futures = dd(set)
def save_future(start=0, num_futures=1, repeat=1):
    for j in range(start, start + num_futures):
        cur = a + str(j)
        for _ in range(repeat):
            cur = get_hash(cur)
        hash_storage[j] = cur
        match5 = re.findall(r"(.)\1\1\1\1", cur)
        for m5 in match5:
            futures[m5].add(j)


def find_index(part2=False):
    keys_found = 0
    for i in range(10**12):
        if i % 1000 == 0:
            print(i)
        if part2:
            save_future(i+1000, num_futures=1, repeat=2017)
        else:
            save_future(i+1000, num_futures=1)
        cur = hash_storage[i]
        match3 = re.findall(r"(.)\1\1", cur)
        if match3 and match3[0] in futures and \
        any(1 <= val - i <= 1000 for val in futures[match3[0]]):
            keys_found += 1
            if keys_found == 64:
                ans(i, should_exit=False)
                break


    # for i in range(30):
        # print(i, hash_storage[i])
#num to hash
hash_storage = {}
#letter to numbers
futures = dd(set)
save_future(start=0, num_futures=1000, repeat=1)
find_index(part2=False)
#num to hash
hash_storage = {}
#letter to numbers
futures = dd(set)
save_future(start=0, num_futures=1000, repeat=2017)
find_index(part2=True)
