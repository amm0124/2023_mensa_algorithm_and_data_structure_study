# 11/26
# 그리디, 정렬
# 백준 1083번 소트: https://www.acmicpc.net/problem/1083
# 접근방법: 내림차순으로 정렬되어야한다. 앞에서부터 가장 큰 수가 먼저
# 채워져야한다. 그런데, 교환의 횟수가 제한되어있으므로,
# 교환할수 있는 범위내에서 최댓값을 찾고, 찾은 최댓값을 가장 앞에 놓는다.
# 이 놓은 수들은 이미 정렬되어있는 수로 보고, 그 뒤의 인덱스부터 교환할수 있는 
# 범위 내의 최댓값을 찾으며 교환권을 다 쓸떄까지 계속 정렬해나간다.

from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split())) 
s = int(stdin.readline())


for i in range(n):
    max_num = max(lst[i:min(n,i+s+1)])
    idx = lst.index(max_num)
    
    for j in range(idx, i, -1):
        lst[j], lst[j-1] = lst[j-1], lst[j]
    
    s -= (idx - i)
    if s<=0:
        break 
print(*lst)
    

