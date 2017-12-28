#AoC Day 17 -- Spinlock
#TIL Spinlocks, Busy-waiting and the blist import, but my sol'n doesnt use it

step = 304 # my input

# Part 1
i = 0
buffer = [0]
for t in range(1,2017+1):
    i = (i + step) % len(buffer) + 1
    buffer[i:i] = [t] 
print(buffer[i-5:i+5])
# Prints [108, 796, 867, 1438, 616, 2017, 1173, 602, 1351, 560]
# so answer is 1173

# Part 2
i = 0
for t in range(1,50000000+1):
    i = (i + step) % t + 1
    if i==1:
        value = t
print(value)
