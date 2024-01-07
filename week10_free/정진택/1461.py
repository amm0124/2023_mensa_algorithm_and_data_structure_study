# 11/2
# 그리디알고리즘
# 백준 1461 도서관: https://www.acmicpc.net/problem/1461
# 접근방법: 양수, 음수 부분에 대해서는 각각 따로 계산해줌. 어차피 원점을 지나야하기때문
# 가장 먼곳은 왕복이 아닌 한번만 가야 유리하므로, 음수 양수 부분에서 각각 절댓값이 가장 큰수를 찾고
# 그 수를 비교했을때 수가 더 적은쪽을 먼저 봄. 예를 들어 양수부분에 젤 큰 수가 있다고 한다면 음수 부분을
# 먼저 봄. 이때 음수부분에서 m개만큼 수들을 묶고, 묶은 수들 중 가장큰 수의 절댓값 * 2를 결과에 더함
# 왕복을 하면서 묶은 좌표에 대해서는 책을 다 놓기때문. 최소를 구해야 하므로 묶을때 큰수부터 먼저 묶어줌
# 그래서 절댓값이 작은 수들은 m개가 아니라 m 이하의 수 개 만큼만 묶일 수 있음. 양수 부분에 대해서도 같은
# 방식으로 진행. 만약 음수부분의 절댓값이 더 크면 반대로 해주면 됨.
from sys import stdin 


n, m = map(int, stdin.readline().split())
books = list(map(int, stdin.readline().split()))
books.sort()

if abs(books[0]) > books[len(books)-1]:
    first = "right"
else:
    first = "left"
res = 0
idx_pos = len(books)
for i in range(n):
    if books[i] > 0:
        idx_pos = i
        break
if first == "right":
    i = len(books)-1
    while i >= idx_pos:
        res += books[i] * 2
        i -= m
    i = 0
    while i < idx_pos:
        res += abs(books[i]) * 2 
        i += m 
    res -= abs(books[0])
else:
    i = 0
    while i < idx_pos:
        res += abs(books[i]) * 2 
        i += m 
    i = len(books)-1
    while i >= idx_pos:
        res += books[i] * 2
        i -= m
   
    res -= books[len(books)-1]
print(res)


