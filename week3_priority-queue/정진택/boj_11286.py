# 7/17
# 우선순위 큐
# 백준 11286번 절댓값 힙 : https://www.acmicpc.net/problem/11286
# 접근방법: 먼저 이중리스트를 만들고 절댓값에 해당하는 인덱스에 있는 리스트에 데이터를 추가하는 방식으로 구현했는데 인덱싱 에러가 남
# 그래서 단일리스트를 만들고 데이터를 우선순위큐에 넣을때마다 정렬을 해봤는데, 역시나 시간초과 남
# heapq모듈을 사용하여 구현

from sys import stdin
import heapq

#인덱싱 에러
# queue = [[]]
# n = int(stdin.readline())
# for i in range(n):
#     num = int(stdin.readline())
#     if num == 0:
#         if queue==[[]]:
#             print(0)
#         else:
#             print(queue[-1].pop())
#     else:
#         queue[abs(num)-1].append(num)
      
#시간초과
# queue = []
# n = int(stdin.readline())
# for _ in range(n):
#     num = int(stdin.readline())
#     if num == 0:
#         if queue==[]:
#             print(0)
#         else:
#             print(queue.pop()[1])
#     else:
#         queue.append([abs(num),num])
#         queue.sort(reverse=True)


n = int(input())
q = []

for i in range(n):
    a = int(stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])