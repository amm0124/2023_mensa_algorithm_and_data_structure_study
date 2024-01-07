# 7/10
# 큐
# 백준 2065번 나룻배: https://www.acmicpc.net/problem/2065
# 접근방법: 해결 못함

location = []
cur_location = "left"
cur_time = 0
m,t,n = map(int, input().split())

for i in range(n):
    time, berth = input().split()
    time = int(time)
    location.append([time, berth])

location.sort()
idx = 0
while idx < n:

    if cur_time < location[idx][0]:
        cur_time += t
        continue
      
    if cur_location != location[idx][1]:
        cur_location = location[idx][1]
        cur_time += t
        continue
    
    else:
        cnt = 0
        while idx < n and cnt < m and cur_location == location[idx][1] and cur_time >= location[idx][0]:
            idx += 1
            cnt += 1

        if cur_location == "left":
            cur_location = "right"
        else:
            cur_location = "left"
        cur_time += t

        for _ in range(cnt):
            print(cur_time)
        
    
    
    
