#9/14
#dfs,브루트포스
#백준 14500번 테트로미노: https://www.acmicpc.net/problem/14500
#접근방법: 모든 노드에 대해서 dfs를 실행시켰다. dfs는 왼쪽,위,오른쪽,아래 모든 방향에 대해 
#재귀적으로 실행되도록 하였다. 그리고 그 깊이가 4가 되면 원래의 최댓값과 비교하여 최대값을 갱신
#시키도록 하였다. ㅗ,ㅓ,ㅏ,ㅜ 모양도 고려해주기 위해 깊이가 2인 곳에서(가운데 부분) 
#dfs를 한번더 진행하도록 하였다. 
#처음에 큐를 이용하여 bfs로 구현했었는데 시간초과가 났었다. 

def dfs(i, j, total,size):
    global ans
    if size == 4:
        ans = max(ans, total)
        return

    for mi, mj in moves:
        ni, nj = i + mi, j + mj

        if 0<= ni < n and 0<= nj < m and not visited[ni][nj]:
            
            if size == 2:
                visited[ni][nj] = True
                dfs(i, j, total+board[ni][nj],size+1)
                visited[ni][nj] = False

            visited[ni][nj] = True
            dfs(ni, nj, total+board[ni][nj],size+1)
            visited[ni][nj] = False


moves=[[-1,0],[0,1],[1,0],[0,-1]]

n,m = map(int, input().split())
visited=[[False for _ in range(m)] for _ in range(n)]
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))
ans=0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,board[i][j],1)
        visited[i][j] = False
print(ans)

