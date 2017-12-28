#AoC Day 13 -- Packet Scanners

import itertools
# depth range
file = """
0: 3
1: 2
2: 4
4: 6
6: 4
8: 6
10: 5
12: 8
14: 8
16: 6
18: 8
20: 6
22: 10
24: 8
26: 12
28: 12
30: 8
32: 12
34: 8
36: 14
38: 12
40: 18
42: 12
44: 12
46: 9
48: 14
50: 18
52: 10
54: 14
56: 12
58: 12
60: 14
64: 14
68: 12
70: 17
72: 14
74: 12
76: 14
78: 14
82: 14
84: 14
94: 14
96: 14
""".strip().split('\n')

def part1(file):
    scanners = dict(
        map(int, line.split(': '))
        for line in file
    )

    sev = 0
    for i in range(93):
        if i not in scanners:
            continue
        r = scanners[i]
        if i % (r * 2 - 2) == 0:
            sev += i * r
    print(sev)

def part2(file):
    scanners = dict(
        map(int, line.split(': '))
        for line in file
    )

    for k, v in scanners.items():
        scanners[k] = v * 2 - 2

    for d in itertools.count(0):
        for key, value in scanners.items():
            if (key + d) % value == 0:
                break
        else:
            print(d)
            break

part1(file)
part2(file)
