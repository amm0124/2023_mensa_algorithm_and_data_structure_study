# 8/29
# 그리디 알고리즘
# 백준 11497번 절댓값 힙 : https://www.acmicpc.net/problem/11497
# 접근방법: 최소 난이도를 갖는 배열을 만들기 위해서는 가장 작은 수가 배열의 0번 인덱스, 
# 그 다음수가 마지막 인덱스에 위치하고 그 다음수들도 똑같이 왼쪽, 오른쪽 순으로 채워지고 가장 큰 수가 
# 정가운데에 위치해야 함을 발견하였다. 그래서 이 규칙대로 새 리스트에 값을 넣어주고 가장큰 간격을 찾아 
# 답을 출력하게 하였다. 

from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    num = int(stdin.readline())
    heights = list(map(int, stdin.readline().split()))
    # 입력값 정렬
    heights.sort()
    # 새 리스트 만듦
    l = [0 for _ in range(len(heights))]
    idx = 0
    max_idx = len(heights) - 1
    # 새 리스트에 값 넣음
    for h in heights:
        l[abs(idx)] = h
        idx = max_idx - idx
        max_idx -= 1
    max_interval = 0
    # 최소 난이도 찾아서 출력
    for i in range(len(l)):
        next = i+1
        if next == len(l):
            next = 0
        interval = abs(l[next] - l[i])
        if interval > max_interval:
            max_interval = interval 
    print(max_interval)    
            
    