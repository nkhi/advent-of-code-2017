# AoC Day 10 -- Knot Hash

file = """
83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100
""".strip()

def part1(lengths):
    LN = 256
    start = list(range(LN))
    lengths = list(map(int, lengths.split(',')))

    pos = 0
    skip = 0
    for ln in lengths:
        back = max(0, pos - LN)
        back2 = max(0, pos + ln - LN)
        st = start[pos: pos + ln] + start[back: back2]
        st = st[::-1]

        top = LN - pos
        if top < 0:
            top = 999

        start[pos: pos + ln] = st[:top]
        start[back: back2] = st[top:]

        pos += ln + skip
        skip += 1
        pos %= LN

    print(start[0] * start[1])


def part2(lengths):
    LN = 256
    start = list(range(LN))
    lengths = list(map(ord, lengths))
    lengths += [17, 31, 73, 47, 23]

    pos = 0
    skip = 0
    for _ in range(64):
        for ln in lengths:
            back = max(0, pos - LN)
            back2 = max(0, pos + ln - LN)
            st = start[pos: pos + ln] + start[back: back2]
            st = st[::-1]

            top = LN - pos
            if top < 0:
                top = 999

            start[pos: pos + ln] = st[:top]
            start[back: back2] = st[top:]

            pos += ln + skip
            skip += 1
            pos %= LN

    accumulator = []
    for i in range(0, 256, 16):
        a = 0
        for c in start[i: i + 16]:
            a ^= c
        accumulator.append(a)
    print(''.join(f'{a:x}' for a in accumulator))

part1(file)
part2(file)