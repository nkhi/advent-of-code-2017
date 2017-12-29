#AoC Day 24 -- Electromagnetic Moat
import collections

file = """
32/31
2/2
0/43
45/15
33/24
20/20
14/42
2/35
50/27
2/17
5/45
3/14
26/1
33/38
29/6
50/32
9/48
36/34
33/50
37/35
12/12
26/13
19/4
5/5
14/46
17/29
45/43
5/0
18/18
41/22
50/3
4/4
17/1
40/7
19/0
33/7
22/48
9/14
50/43
26/29
19/33
46/31
3/16
29/46
16/0
34/17
31/7
5/27
7/4
49/49
14/21
50/9
14/44
29/29
13/38
31/11
""".strip().split('\n')

def part1(start):
    q = collections.deque([(0, start, 0)])
    while q:
        nxt, pins, ttl = q.popleft()

        p = 0
        for (k1, k2), v in pins.items():
            if not v:
                continue
            if k1 == nxt:
                p = 1
                tmp = collections.Counter(pins)
                tmp[k2, k1] -= 1
                tmp[k1, k2] -= 1
                q.append((k2, tmp, ttl + k2 + k1))
        if not p:
            yield ttl


def part2(start):
    q = collections.deque([(0, start, 0, 0)])
    while q:
        nxt, pins, ttl, ll = q.popleft()

        p = 0
        for (k1, k2), v in pins.items():
            if not v:
                continue
            if k1 == nxt:
                p = 1
                tmp = collections.Counter(pins)
                tmp[k2, k1] -= 1
                tmp[k1, k2] -= 1
                q.append((k2, tmp, ttl + k2 + k1, ll + 1))
        if not p:
            yield ll, ttl


def main(file):
    pins = collections.Counter()
    for line in file:
        x, y = map(int, line.split('/'))
        pins[x, y] += 1
        pins[y, x] += 1

    print(max(part1(pins)))
    print(max(part2(pins))[1])


main(file)