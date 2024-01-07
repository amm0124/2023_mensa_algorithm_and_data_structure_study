# 11/16
# bfs
# 백준 1325번 램프: https://www.acmicpc.net/problem/1325
# 접근방법: 한번에 가장 많은 컴퓨터를 해킹하기 위해서는 가장 신뢰를 많이 받는
# 컴퓨터를 찾아야한다. 이를 그래프에 적용하면, 자손노드가 가장 많은 노드를 찾으면 된다.
# 그래서 문제에 주어진 그래프를 bfs탐색하면서 방문한 노드들의 개수를 카운트해주었다.
# 방문이 끝나면 각 노드별로 방문한 자손노드들의 개수를 저장하고, 그 수가 가장 많은 노드들을
# 순서대로 출력해주었다.
# 이 문제 메모리초과 때문에 막 쉽진않았음
# dfs는 재귀함수의 오버헤드 때문에 bfs보다 검색속도가 약간 느리다고해서 시간초과가 날수도있다.

from sys import stdin 
from collections import deque

m, n = map(int, stdin.readline().split())
graph = [[] for _ in range(m+1)]

# 문제에 주어진 입력을 그래프로 만들어줌
for _ in range(n):
    a,b = map(int, stdin.readline().split())
    graph[b].append(a)

# 각 노드별 자손노드 갯수 저장 
node_count = [0] * (m+1)

def bfs(graph, start_node): #그래프와 시작 노드를 받음
    visited = [False] * (m+1) #방문한 노드들
    visited[start_node] = True
    need_visited = deque([start_node]) #아직 방문안한 노드들
    count = 1

    while need_visited: #자손노드 모두 방문할떄까지
        start_node = need_visited.popleft()
        for child in graph[start_node]:
            if not visited[child]: #아직 방문안했다면
                visited[child] = True #방문
                need_visited.append(child) 
                count += 1 #카운트
    return count
        

result = []
for start in range(1, len(graph)):
    result.append(bfs(graph, start)) #각 노드별 카운트
 
for i in range(len(result)):
    if max(result) == result[i]:
        print(i + 1, end=' ')
