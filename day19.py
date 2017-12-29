#AoC Day 19 -- A series of tubes
#This problem was pretty conceptually challenging, so I broke it into a lot of
#subproblems

opened = open("day19.txt", 'r').read()
lines = opened.splitlines()

x = 0
y = 0
d = 0
out = ""
count = 0

while lines[y][x] == " ":
  x += 1

while True:
  if lines[y][x] == " ":
    break # Sorry
  count += 1
  if lines[y][x] == "+":
    if d in [0, 2]:
      if x > 0 and lines[y][x-1] is not " ":
        d = 3
      elif x < len(lines[y])-1 and lines[y][x+1] is not " ":
        d = 1
    else:
      if y > 0 and lines[y-1][x] is not " ":
        d = 2
      elif y < len(lines)-1 and lines[y+1][x] is not " ":
        d = 0
  elif lines[y][x].isalpha():
    out += lines[y][x]
  if d == 0:
    y += 1
  elif d == 1:
    x += 1
  elif d == 2:
    y -= 1
  elif d == 3:
    x -= 1

print(out)
print(count)

