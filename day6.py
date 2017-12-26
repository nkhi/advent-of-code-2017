# AoC Day 6 -- Memory Allocation

puzzle_input = """
4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5
""".strip().split()
tup = tuple(int(num) for num in puzzle_input)
seen = {}
muts = list(tup)

while tup not in seen:
    seen[tup] = len(seen)
    length = len(muts)
    i, e = max(enumerate(muts), key=lambda x: x[1])
    muts[i] = 0
    while e:
        i = (i + 1) % length
        muts[i] += 1
        e -= 1
    tup = tuple(muts)

# Part 1

print(len(seen))

# Part 2

print(len(seen) - seen[tup])