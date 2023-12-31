"""
Code explanation

1. 우선 받기전 그냥 수를 받을 리스트, 그리고 mod개 (0~mod-1)까지 수가 나왔는지, 언제 나와서 몇번째 인덱스에 존재하는지 확인하는 이중리스트 를 생성한다
2. 1 num 이 나올 경우 mod로 나눠 나머지를 저장하고, 이 나머지의 리스트 (예를 들어 나머지가 3이면 3의 리스트)에 지금 몇번째 나온 수인지 인덱스를 저장한다.
3. 2는 그냥 pop 하면서 저장한거 빼고, 인덱스 저장한거 뺀다.
4-1. 3의 경우가 중요한데, 뒤에서부터 순서대로 다나왔는지 확인하니까 최악의 경우는 리스트 전체를 다봐야 하는 경우라 min_count = len(arr)로 설정한다.
4-2. 그리고 우선 나머지가 한번씩은 나와야 되니까 이중 리스트 돌면서 리스트가 빈경우가 있다면 -1하고 끝낸다.
4-3. 만약 모두 있다면, 어디까지가 최소로 나와야 성립하는지 알아야 하니까, 각 나머지 리스트마다 최대 인덱스 (여기서는 따라서 그 나머지 리스트의 -1번째 (마지막) 인덱스)를 뽑고, 이것과 현재 min_count 중 더 작은걸 저장한다. (최소로 나와야 하는 거니까 더 작은걸 골라야함)
4-4. 모든 나머지 리스트를 돌고, 최소 여기 인덱스까지 나와야한다 = min_count를 뽑으면 이걸 전체 길이에서 빼서 갯수를 찾는다.

"""

import sys

q, mod = map(int, sys.stdin.readline().split())
# 전체 스택 리스트
arr = []

# mod 나머지 리스트
dp = [[] for _ in range(mod)]

for _ in range(q):
    query = sys.stdin.readline().split()
    # 1인 경우
    if query[0] == '1':
        # 해당 mod 리스트에 인덱스 추가
        dp[int(query[1]) % mod].append(len(arr))
        # 값도 추가
        arr.append(int(query[1]) % mod)
    elif query[0] == '2':
        if arr:
            x = arr.pop()
            dp[x].pop()
    else:
        # 최대는 내 스택 길이
        min_count = len(arr)
        check = True
        for x in dp:
            # 빈경우는 어차피 안되니까 -1
            if not x:
                print(-1)
                check = False
                break
            # 현재 mod 기준 최대 index 가져오기 , 지나가면서 최소 index로 이동
            min_count = min(x[-1], min_count)
        if check:
            print(len(arr) - min_count)
