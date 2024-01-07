# 8/4
# 다익스트라 알고리즘
# 백준 1446번 지름길: https://www.acmicpc.net/problem/1446
# 접근방법: 거리를 담는 리스트를 만들고
# 지름길을 만나면 해당 인덱스의 거리를 바꿈
# 예를 들어 10에서 60까지 거리가 40인 경우, 60번째 인덱스의 값을
# 10+40인 50으로 바꾸고 그 이후에 값들도 업데이트함
# 마지막엔 마지막 인덱스의 값을 출력

from sys import stdin

# 입력받기
n, d = map(int, stdin.readline().split())
li = [list(map(int,stdin.readline().split())) for _ in range(n)]

# 최단거리담는 그래프 
graph = [i for i in range(d+1)]

for i in range(d+1):
    # 지름길 있으면 최단거리 바꿈
    graph[i] = min(graph[i],graph[i-1]+1)
    for s,e,l in li:
        if i == s and e <= d:
            graph[e] = min(graph[e],graph[i]+l)

print(graph[-1])
