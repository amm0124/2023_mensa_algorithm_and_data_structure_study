# 9/9

from sys import stdin 
from collections import deque
m, n = map(int, stdin.readline().split())

box = []
for _ in range(n):
    box.append(list(map(int,stdin.readline().split())))
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                queue.append((nx,ny))
                box[nx][ny] = box[x][y]+1
res=0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)