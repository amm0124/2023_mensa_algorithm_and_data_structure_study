# 9/22
# 큐
# 백준 2065번 나룻배: https://www.acmicpc.net/problem/2065
# 접근방법: 대기열과 배에 대한 큐를 만들어둠. 출력이 n번 될 때까지
# while문을 돌면서 현재 시간이하인 시간들을 먼저 다 대기열에 넣고
# 다음으로 현재 배의 위치와 같은 대기열에 있는 사람들을 모두 배로 태움
# 모두는 아니고, m만큼 태움. 만약 대기열이나 배에 변화가 있다면
# 현재 배의 방향을 바꿔줌. 시간은 항상 늘려줌
# 문제 조건이 입력받은 순서대로 도착하게 되는 시간을 출력하라이므로
# res라는 리스트에 while문을 돌때마다 현재시간을 넣어주는데
# 입력받은 순서에 맞게 인덱스를 주면서 값을 넣어주고 마지막에 출력해줌
# 출력은 똑같이 나오는데, 계속 틀렸다고 나오긴함

from sys import stdin 
from collections import deque
m,t,n = map(int, stdin.readline().split())

q = []

for i in range(n):
    time, direct = stdin.readline().rstrip().split()
    time = int(time)
    q.append((time, direct,i))
q.sort()

stop = [deque(),deque()]
ship = deque()

now_side = 0
now_time = 0
cnt = 0
res = [0]*n

while(cnt < n):
    chk = 0
    while q and q[0][0] <= now_time:
        side = (q[0][1] == "right")
        stop[side].appendleft((q.pop(0))[2])
        chk = 1
    while len(ship) < m and stop[now_side]:
        ship.appendleft(stop[now_side].pop())
        chk = 1

    if chk:
        now_side = 1-now_side
    now_time += t
   
    while ship:
        res[ship.popleft()] = now_time
        cnt += 1

for i in res:
    print(i)


    
    