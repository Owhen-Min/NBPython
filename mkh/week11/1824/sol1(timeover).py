from collections import deque
# 39번까지만 ㅠㅠ

def move(y, x, mem, dir):
    global poss_go
    y += deltas[dir][0]
    x += deltas[dir][1]
    if 0 <= y < R and 0 <= x < C:
        poss_go.append((y, x, mem, dir))
    elif y == R:
        poss_go.append((0, x, mem, dir))
    elif x == C:
        poss_go.append((y, 0, mem, dir))
    elif y == -1:
        poss_go.append((R-1, x, mem, dir))
    elif x == -1:
        poss_go.append((y, C-1, mem, dir))


T = int(input())
deltas = [[0, 1], [1,0], [0, -1], [-1,0]]       # 우 하 좌 상

for tc in range(1, T+1):
    result = ['NO', 'YES']
    R, C = map(int,input().split())
    board = [input() for _ in range(R)]
    flag = False
    poss_go = deque()
    poss_go.append((0, 0, 0, 0))        # y, x, memory, direction
    visited = deque()
    for row in board:
        if '@' in row:
            break
    else: poss_go = None
    while poss_go:
        y, x, mem, dir = poss_go.popleft()
        if (y, x, mem, dir) in visited:
            continue
        else:
            visited.append((y, x, mem, dir))

        res = board[y][x]

        if res == '@':
            flag = 1
            break

        elif res.isdigit():
            mem = int(res)
            move(y, x, mem, dir)

        elif res == '-':
            mem = (mem-1)%16
            move(y, x, mem, dir)

        elif res == '+':
            mem = (mem+1)%16
            move(y, x, mem, dir)

        elif res == '.':
            move(y, x, mem, dir)

        elif res == '_':
            if mem: move(y, x, mem, 2)
            else: move(y, x, mem, 0)

        elif res == '|':
            if mem: move(y, x, mem, 3)
            else: move(y, x, mem, 1)

        elif res == '<':
            move(y, x, mem, 2)

        elif res == '>':
            move(y, x, mem, 0)

        elif res == '^':
            move(y, x, mem, 3)

        elif res == 'v':
            move(y, x, mem, 1)

        else:
            for i in range(4):
                move(y, x, mem, i)

    print(f'#{tc} {result[flag]}')
