# 9/6

from sys import stdin

n,m = map(int, stdin.readline().split())

board = []
b_board = """BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB"""
w_board = """WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW"""
b_board = b_board.split('\n')
w_board = w_board.split('\n')

for _ in range(n):
    line = list(stdin.readline().rstrip())
    board.append(line)

cnt_lst = []
for a in range(n-7):
    for b in range(m-7):
        b_cnt = 0
        w_cnt = 0
        for i in range(8):
            for j in range(8):
                if board[i+a][j+b] != b_board[i][j]:
                    b_cnt += 1      
                if board[i+a][j+b] != w_board[i][j]:
                    w_cnt += 1           
        cnt_lst.append(b_cnt)     
        cnt_lst.append(w_cnt)      

print(min(cnt_lst))