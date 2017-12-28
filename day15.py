#AoC Day 15 -- Dueling Generators
# 20ish second rt

a = 699
b = 124
guard = 0xffff
count = 0
count2 = 0
for i in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if (a & guard) == (b & guard):
        count += 1
print(count)

for i in range(5000000):
    a = (a * 16807) % 2147483647
    while a % 4:
        a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    while b % 8:
        b = (b * 48271) % 2147483647
    if (a & guard) == (b & guard):
        count2 += 1
print(count2)
