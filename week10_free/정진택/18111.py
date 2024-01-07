# 9/9

from sys import stdin 
n,m,b = map(int, stdin.readline().split())
block = []
for _ in range(n):
    block.append(list(map(int, stdin.readline().rstrip().split())))

mtime = 100000000000
idx = 0
for i in range(257):
    keep = 0 
    use = 0

    for x in range(n):
        for y in range(m):
            if block[x][y] > i:
                keep += block[x][y] - i
            else:
                use += i - block[x][y] 

    if use > keep + b:
        continue

    time = keep *2 + use
    if mtime >= time:
        mtime = time
        idx = i 

print(mtime, idx)
