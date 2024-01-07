#8/10
#그래프
#백준 1238번 파티: https://www.acmicpc.net/problem/1238
#접근방법: 다익스트라 알고리즘을 활용하여 각 노드에서 x번까지 가는 최단거리와
#돌아오는 최단거리를 구하고 그 합의 최솟값을 출력하도록 함
#다익스트라 함수에서 각 노드까지의 최단거리는 distance변수에 담고
#이미 이동한 노드는 heap에 담으며, heap이 빌때까지 while문을 돌며 최단거리를 찾았다.
#heapq를 쓰기 전에는 시간초과가 났음

from sys import stdin
import heapq

n,m,x = map(int, stdin.readline().split())
li = [[]for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int, stdin.readline().split())
    li[s].append([e,t])

#거리 짧은 순으로 정렬
for l in li:
    l.sort(key=lambda x: x[1])

INF=10000000
def dijkstra(start):
    # 이동한 정점들과 거리를 담음 
    q = []
    heapq.heappush(q,[0,start])
    # 각 정점까지 거리 담음
    distance = [INF] * (n+1)
    distance[start] = 0
    
    while q:
        dis, now = heapq.heappop(q)

        # 이미 계산한 거리보다 더 크면 무시
        if distance[now] < dis:
            continue

        # 방문한 노드에서 다음 방문할 노드들을 탐색
        for nod, cos in li[now]:
            # 현재 노드까지 거리와 다음 노드까지 거리 합함
            cost = dis + cos
            # 최단거리 찾으면 저장하고 방문
            if distance[nod] > cost:
                distance[nod] = cost
                heapq.heappush(q,[cost,nod])
    return distance

result = 0
for i in range(1,n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x]+back[i])
print(result)
    

