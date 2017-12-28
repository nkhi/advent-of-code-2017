# AoC Day 9 -- Stream Processing

opened = open("day9.txt", "r")
file = opened.read()

def main(file):
    o = 0
    garb = False
    total = 0
    current = 0
    file = iter(file)
    total2 = 0
    for c in file:
        if garb:
            if c == '!':
                next(file)
            elif c == '>':
                garb = False
            else:
                total2 += 1
        else:
            if c == '{':
                current += 1
                total += current
            elif c == '}':
                current -= 1
            elif c == '<':
                garb = True
    print(total)
    print(total2)


main(file)