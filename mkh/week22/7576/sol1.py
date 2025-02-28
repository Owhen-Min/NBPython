deltas = ((1,0), (-1,0), (0, 1), (0, -1))

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
unripe, ripe, temp = set(), set(), set()
ans = 0

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 0: unripe.add((i, j))
        elif tomatos[i][j] == 1: ripe.add((i, j))

while unripe:
    if not ripe:
        ans = -1
        break

    for y, x in ripe:
        for dy, dx in deltas:
            if 0 <= y+dy < N and 0 <= x+dx < M and (y+dy, x+dx) in unripe:
                unripe.remove((y+dy, x+dx))
                temp.add((y+dy, x+dx))

    ripe = temp
    temp = set()
    ans += 1

print(ans)
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
ans = 8
'''