import sys
from itertools import combinations

def cal_dist(house, combi):
    y, x = house
    return min(abs(y-i)+abs(x-j) for i, j in combi)


n, m = map(int,input().split())
board = [list(sys.stdin.readline().split()) for _ in range(n)]
hs = []
ch = []

for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            hs.append((i, j))
        elif board[i][j] == '2':
            ch.append((i, j))

ans = 1e9

for combi in combinations(ch, m):
    dists = 0
    for house in hs:
        dists += cal_dist(house, combi)
    if ans > dists:
        ans = dists

print(ans)