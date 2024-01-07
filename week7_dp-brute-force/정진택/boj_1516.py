# 8/16
# 다이나믹 프로그래밍, 위상정렬
# 백준 1516번 지름길: https://www.acmicpc.net/problem/1516
# 접근방법: 처음에는 시간과 이전번호 리스트를 각각 만들어 반복문을 통해 값을 넣어주고 또 반복문을 돌며 시간 리스트의 값들을 바꿔주는 식으로 했는데, 인덱스 에러 나옴
# 그래서 그래프를 이용하여 접근함
# 시간 리스트, 정답 시간 리스트, 접근차수(위상정렬), 그래프, 큐를 만들고
# 처음에 시간 리스트에 기본값들을 넣고 그래프에 다음 정점들을 넣어두고 그때마다 차수에 1씩 더해줌
# 차수가 0인 정점들을 큐에 넣고 큐에서 정점들을 빼면서 다음 연결된 정점들에 대한 정답 시간 리스트 값을 변경해줌
# 이때 차수도 하나씩 감소시키고 차수가 0이라면 큐에 넣어줌
# 큐가 비게 되면 정답 시간 리스트 값이 다 바뀌게 되고 이를 출력해줌 

from sys import stdin

n = int(stdin.readline())
time_lst = [0] * (n+1)
degree = [0] * (n+1)
new_time_lst = [0] * (n+1)
graph = [[] for _ in range(n + 1)]
queue = []

for i in range(1, n+1):
    input_lst = list(map(int, stdin.readline().split()))
    time_lst[i] = input_lst[0]
    for j in input_lst[1:-1]:
        graph[j].append(i)
        degree[i] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)
        new_time_lst[i] = time_lst[i]

while queue:
    now = queue.pop(0)
    for i in graph[now]:
        degree[i] -= 1
        new_time_lst[i] = max(new_time_lst[i], new_time_lst[now] + time_lst[i])
        if degree[i] == 0:
            queue.append(i)

for i in range(1, len(new_time_lst)):
    print(new_time_lst[i])

# from sys import stdin

# n_lst = [0]
# n = int(stdin.readline())
# before_lst = [[] for _ in range(n+1)]

# for j in range(n):
#     input_lst = list(map(int, stdin.readline().split()))
#     time = input_lst[0]
#     before = []
#     if len(input_lst) > 2:
#         for i in range(1, len(input_lst)-1):
#             time += n_lst[input_lst[i]]
#             before.append(input_lst[i])
#     before_lst[j+1] = before
#     n_lst.append(time)

# for i in range(1, len(before_lst)):
#     for j in before_lst[i]:
#         for k in range(len(before_lst[i])):
#             if before_lst[i][k] in before_lst[j]:               
#                 n_lst[i] -= n_lst[before_lst[i][k]] 

# for i in range(1, len(n_lst)):
#     print(n_lst[i])
