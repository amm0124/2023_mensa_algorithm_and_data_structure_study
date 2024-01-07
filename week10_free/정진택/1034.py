#9/14
#브루트포스
#백준 1034번 램프: https://www.acmicpc.net/problem/1034
#접근방법:각 행에 대해서 0의 개수를 센 후에 스위치를 누르는 횟수와 비교하여
#0의 개수가 더 작거나 같고 같이 홀수이거나 같이 짝수일경우 스위치를 누르면 그 행의
#램프를 모두 킬수있으므로, 반복문을 통해 모든 행을 또 돌면서 같은 행이 있는지 센다.
#행이 같으면 이 행도 모두 킬수 있게 되므로 카운트에 1씩 더해준다. 이 과정을 
# 모든 행에 대해 반복하면서 최댓값을 갱신한다. 

from sys import stdin 
n,m = map(int, stdin.readline().split())
lamp = []
for _ in range(n):
    lamp.append(list(stdin.readline().rstrip()))
k = int(stdin.readline())
max_cnt = 0

for i in range(n):
    zero_cnt = 0
    for num in lamp[i]:
        if num == '0':
            zero_cnt += 1
    same_cnt = 0
    if zero_cnt <=k and zero_cnt%2 == k%2:
        for j in range(n):
            if lamp[i] == lamp[j]:
                same_cnt += 1
    max_cnt = max(max_cnt, same_cnt)
print(max_cnt)