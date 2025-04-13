from collections import deque
import copy

class IcebergSimulator:
    def __init__(self, grid: list[list[int]], n: int, m: int):
        self.grid = grid
        self.n = n
        self.m = m
        self.year = 0
        self.delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def count_sea_neighbors(self, x, y):
        """상하좌우에 인접한 바다(0)의 개수를 셈"""
        count = 0
        for dx, dy in self.delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.m:
                if self.grid[nx][ny] == 0:
                    count += 1
        return count

    def melt(self):
        """빙산 녹이기: 한 해에 상하좌우 바다 수만큼 빙산을 줄임"""
        new_grid = copy.deepcopy(self.grid)
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] > 0:
                    sea_count = self.count_sea_neighbors(i, j)
                    new_grid[i][j] = max(0, self.grid[i][j] - sea_count)
        self.grid = new_grid
        self.year += 1

    def count_icebergs(self):
        """빙산 덩어리 개수를 구함 (BFS 사용)"""
        visited = [[False] * self.m for _ in range(self.n)]
        count = 0

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] > 0 and not visited[i][j]:
                    self.bfs(i, j, visited)
                    count += 1
        return count

    def bfs(self, x, y, visited):
        """빙산 탐색용 BFS"""
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in self.delta:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.n and 0 <= ny < self.m:
                    if self.grid[nx][ny] > 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    def simulate(self):
        """전체 시뮬레이션 실행: 분리될 때까지 반복"""
        while True:
            count = self.count_icebergs()
            if count == 0:
                return 0
            if count >= 2:
                return self.year
            self.melt()

# 테스트 실행
if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    simulator = IcebergSimulator(grid, n, m)
    result = simulator.simulate()
    print(result)
