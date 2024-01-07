#12/3
#bfs
#백준 1043번 거짓말: https://www.acmicpc.net/problem/1043
#접근방법: 같은 파티에 참여하는 사람들을 그래프를 통해 이어주고
#노드가 연결되어있을때, 진실을 아는 노드가 있다면 연결된 노드들도 다 진실을 알게 한다.
#그래프와 bfs로 이문제를 해결하였다.
from sys import stdin  
from collections import deque

n,m = map(int, stdin.readline().split())
knows = list(map(int, stdin.readline().split()))

#각 사람별로 진실을 아는지
know_person = [False for _ in range(n+1)]

#같은 파티 참여하는 사람들 연결
graph = [[] for _ in range(n+1)]
parties = []

for i in range(m):
    lst = list(map(int, stdin.readline().split()))
    n, party = lst[0],lst[1:]
    parties.append(party)

    #같은 파티 참여하는 사람들 연결
    for j in range(n):
        for k in range(j+1, n):
            graph[party[j]].append(party[k])
            graph[party[k]].append(party[j])

# 중복 제거
graph = [list(set(x)) for x in graph]

if knows == [0]:
    print(m)
    exit(0)

for know in knows[1:]:
    know_person[know] = True


def bfs(x): #x는 진실을 아는 사람들이 리스트형태로 들어온다
    q = deque(x)
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not know_person[next]:
                know_person[next] = True
                q.append(next)

bfs([x for x in range(1, len(know_person)) if know_person[x]])
know_person = [x for x in range(1, len(know_person)) if know_person[x]]
cnt = 0


for party in parties:
    if not (set(party) & set(know_person)): #교집합 연산을 통해 party에서 한명이라도 진실을 아는 사람이 있으면 cnt 추가 x
        cnt +=1 
print(cnt)
