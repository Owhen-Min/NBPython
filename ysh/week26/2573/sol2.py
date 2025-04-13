from collections import deque
from typing import List, Tuple

class IcebergSimulator:
    # 상하좌우 4방향 이동을 위한 상수
    DELTA: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, grid: List[List[int]], n: int, m: int) -> None:
        # 빙산의 초기 상태 및 관련 변수 초기화
        self.grid = grid
        self.n = n
        self.m = m
        self.year = 0  # 경과 연도
        self.ice_positions = [  # 현재 빙산이 존재하는 좌표 리스트
            (i, j) for i in range(n) for j in range(m) if grid[i][j] > 0
        ]
        self.visited = [[False] * m for _ in range(n)]  # BFS용 방문 여부 기록

    @staticmethod
    def count_sea_neighbors(x: int, y: int, grid: List[List[int]], delta: List[Tuple[int, int]]) -> int:
        """
        현재 좌표(x, y)의 상하좌우에서 바다(0)의 개수를 센다.
        - grid 상태를 직접 인자로 받아 외부 의존성을 제거함
        """
        n, m = len(grid), len(grid[0])
        count = 0
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if not grid[nx][ny] and 0 <= nx < n and 0 <= ny < m: # ← 주의: 조건 순서 중요
                count += 1
        return count

    def melt(self) -> None:
        """
        1년이 지나며 빙산이 녹는 과정을 시뮬레이션
        - 각 빙산 위치에 대해 주변 바다 수만큼 높이를 감소시킨다.
        - 동시에 빙산이 남아 있는 위치만 다시 추적한다.
        """
        next_grid = [row[:] for row in self.grid]
        new_ice_positions = []

        for x, y in self.ice_positions:
            sea = self.count_sea_neighbors(x, y, self.grid, self.DELTA)
            new_height = max(0, self.grid[x][y] - sea)
            next_grid[x][y] = new_height
            if new_height > 0:
                new_ice_positions.append((x, y))

        self.grid = next_grid
        self.ice_positions = new_ice_positions
        self.year += 1

    def count_icebergs(self) -> int:
        """
        현재 빙산이 몇 개의 덩어리로 분리되어 있는지 계산
        - BFS를 이용하여 연결된 빙산을 하나의 덩어리로 간주한다.
        """
        for i, j in self.ice_positions:
            self.visited[i][j] = False

        count = 0
        for i, j in self.ice_positions:
            if not self.visited[i][j]:
                self._bfs(i, j)
                count += 1
        return count

    def _bfs(self, x: int, y: int) -> None:
        """
        BFS를 통해 한 덩어리에 포함되는 빙산을 모두 방문 처리
        """
        queue = deque([(x, y)])
        self.visited[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in self.DELTA:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.n and 0 <= ny < self.m:
                    if self.grid[nx][ny] > 0 and not self.visited[nx][ny]:
                        self.visited[nx][ny] = True
                        queue.append((nx, ny))

    def simulate(self) -> int:
        """
        매년 빙산을 녹이며 덩어리 수를 확인하고,
        두 덩어리 이상으로 분리되는 첫 해를 반환
        - 끝까지 분리되지 않고 모두 녹으면 0을 반환
        """
        while self.ice_positions:
            if self.count_icebergs() >= 2:
                return self.year
            self.melt()
        return 0

    @classmethod
    def from_input(cls) -> 'IcebergSimulator':
        """
        표준 입력으로부터 빙산 데이터를 받아 시뮬레이터 인스턴스를 생성
        """
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        return cls(grid, n, m)


if __name__ == "__main__":
    # 시뮬레이션 실행 및 결과 출력
    simulator = IcebergSimulator.from_input()
    print(simulator.simulate())
