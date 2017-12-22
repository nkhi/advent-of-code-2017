#AoC Day 2 -- Spiral Memory

inputt = 325489

#Part 1
def part1(inputt):
    direction = -1
    count = 1
    x = 0
    y = 0
    i = 1
    while i <= inputt:
        for _ in range(count):
            i += 1
            x += direction
            if i == inputt:
                return x, y
        for _ in range(count):
            i += 1
            y += direction
            if i == inputt:
                return x, y
        direction *= -1
        count += 1

#Part 2
def part2(inputt):
    direction = -1
    count = 1
    x = 0
    y = 0
    i = 1
    guide = {(0, 0): 1}
    while i <= inputt:
        for _ in range(count):
            x += direction
            guide[x, y] = sum(
                guide[dx, dy]
                for dx in range(x - 1, x + 2)
                for dy in range(y - 1, y + 2)
                if (dx, dy) in guide
            )
            if guide[x, y] >= inputt:
                return guide[x, y]
        for _ in range(count):
            y += direction
            guide[x, y] = sum(
                guide[dx, dy]
                for dx in range(x - 1, x + 2)
                for dy in range(y - 1, y + 2)
                if (dx, dy) in guide
            )
            if guide[x, y] >= inputt:
                return guide[x, y]
        direction *= -1
        count += 1

x, y = part1(inputt)
print(abs(x) + abs(y))
print(part2(inputt))