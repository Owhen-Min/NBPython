from collections import deque, defaultdict

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# BFS 함수
def bfs(sy: int, sx: int, farm: list, visited: list, n: int, m: int) -> None:
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if farm[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

# 메인 로직 함수
def solution(t: int) -> defaultdict:
    result = defaultdict(int)
    for i in range(1, t + 1):
        m, n, k = map(int, input().split())  # 가로, 세로, 배추 개수
        farm = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            farm[y][x] = 1

        for y in range(n):
            for x in range(m):
                if farm[y][x] == 1 and visited[y][x] == 0:
                    bfs(y, x, farm, visited, n, m)
                    result[i] += 1  # 지렁이 한 마리 필요
    return result

# 실행부
if __name__ == "__main__":
    test_case = int(input())
    solution = solution(test_case)
    for val in solution.values():
        print(val)
