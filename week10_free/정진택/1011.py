#11/12
#수학
#백준 1011번 램프: https://www.acmicpc.net/problem/1011
#접근방법: 처음과 마지막은 1광년만 이동할 수 있고, 그 사이는 최대한 많이 이동하는게
#좋으므로, 시작점(a)과 도착점(b)에서 1,2,3,...씩 등차수열로 이동하면서 카운트를 센다
#그러다가 a와b가 서로 역전될때 카운트를 멈추면 되는데, 만약 역전되기 직전의 거리가
#한번에 갈 수 있는 거리면 카운트에 1을 더하고, 한번에 가지 못하면 카운트에 2를 더한다.
 
from sys import stdin
n = int(stdin.readline())
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    a = x 
    b = y
    l = 0
    r = 0 
    cnt = 0
    while True:
        l += 1
        a = a + l
        if a >= b:
             cnt += 1
             break 

        r += 1
        b = b - r 

        if a >= b:
                cnt +=2 
                break
        
        cnt += 2
     
    print(cnt)
        


