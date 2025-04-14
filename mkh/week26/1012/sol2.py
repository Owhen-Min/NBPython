import sys

input = sys.stdin.readline
deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        for dx, dy in deltas:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in cabbages and (nx, ny) not in visited:
                stack.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    cabbages = {tuple(map(int, input().split())) for _ in range(k)}
    visited = set()

    count = 0
    for cabbage in cabbages:
        if cabbage not in visited:
            dfs(*cabbage)
            count += 1

    print(count)