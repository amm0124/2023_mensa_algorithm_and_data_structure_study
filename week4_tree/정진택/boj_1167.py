#7/21
#트리
#백준 1167번 트리의 지름: https://www.acmicpc.net/problem/1167
#접근방법: 리스트 안에 정점+1개의 리스트들을 넣을 수 있는 트리 변수를 만들고, 노드 번호를 인덱스로 하여 해당 인덱스의 리스트에 연결된 노드번호와
#거리로 이루어진 쌍의 리스트를 추가한다. 방문표시를 위해 정점+1개의 리스트를 만들고, 임의의 노드에서 dfs를 진행한 후 가장 먼
# 노드에서부터 다시 dfs를 진행하여, 트리의 지름을 구한다. dfs함수는 재귀형식으로 만들고 방문을 하면 방문한 노드번호와 쌓인 거리를 인자로 하여 dfs함수를
# 재귀적으로 호출가능하게 한다. 그리하여 노드 사이에 거리를 구할 수 있는것이다. 
#그래프는 노드와 간선이 연결되어있는 구조, 트리는 사이클이 없는 연결 그래프

from sys import stdin

def dfs(x,y):
    for a,b in tree[x]:
        if visited[a] == -1:
            visited[a] = b+y
            dfs(a,b+y)

v = int(stdin.readline())
tree = [[]for _ in range(v+1)]
for i in range(v):
    n = list(map(int,stdin.readline().split()))
    for j in range(1,len(n)-2,2):
        tree[n[0]].append([n[j],n[j+1]]) 
        # 노드 번호를 인덱스로 하여 해당 인덱스의 리스트에 연결된 노드와 거리 쌍의 리스트를 추가

# tree = [[], [[3, 2]], [[4, 4]], [[1, 2], [4, 3]], [[2, 4], [3, 3], [5, 6]], [[4, 6]]]

visited = [-1] * (v+1)
visited[1] = 0
dfs(1,0)

start = visited.index(max(visited))
visited = [-1]*(v+1)
visited[start] = 0
dfs(start,0)

print(max(visited))
