from typing import List, Tuple

class SnailSimulator:
    # 상, 우, 하, 좌 순서로 움직이기 위한 방향 벡터
    DELTA: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, size: int, find_number: int) -> None:
        """
        시뮬레이터 초기화
        :param size: 격자 크기 (n x n)
        :param find_number: 위치를 찾고 싶은 숫자
        """
        self.size = size
        self.find_number = find_number
        self.grid = [[0] * size for _ in range(size)]  # 결과를 채울 격자
        self.position = (0, 0)  # 찾는 숫자의 좌표 (1-indexed)

    def run(self) -> None:
        """
        달팽이 숫자 채우기 시뮬레이션 실행
        - 가운데에서 시작해 시계 방향으로 회전하며 숫자를 채움
        """
        y, x = self.size // 2, self.size // 2  # 시작 위치: 격자 중앙
        self.grid[y][x] = 1  # 시작 숫자
        if self.find_number == 1:
            self.position = (y + 1, x + 1)  # 결과는 1-indexed로 반환

        cur_num = 2
        cur_step = 1  # 현재 방향에서 몇 칸 이동할지
        while cur_num <= self.size * self.size:
            for direction in range(4):  # 상우하좌 순서로 회전
                dy, dx = SnailSimulator.DELTA[direction]
                for _ in range(cur_step):
                    if cur_num > self.size * self.size:
                        return  # 모두 채웠으면 종료
                    y += dy
                    x += dx
                    self.grid[y][x] = cur_num
                    if cur_num == self.find_number:
                        self.position = (y + 1, x + 1)  # 위치 저장 (1-indexed)
                    cur_num += 1
                if direction % 2 == 1:
                    cur_step += 1  # 두 방향마다 한 칸씩 증가 (달팽이 모양)

    def get_result(self) -> dict:
        """
        현재 상태에서 결과를 사전 형태로 반환
        :return: {'grid': 숫자 채워진 2차원 배열, 'position': 찾는 숫자의 위치}
        """
        return {
            'grid': self.grid,
            'position': list(self.position)
        }

    def simulate(self) -> dict:
        """
        run + get_result를 한번에 실행하는 통합 메서드
        """
        self.run()
        return self.get_result()

    @classmethod
    def from_input(cls) -> 'SnailSimulator':
        """
        사용자 입력을 통해 시뮬레이터 인스턴스를 생성
        :return: SnailSimulator 인스턴스
        """
        size = int(input())          # 홀수 크기의 격자
        target = int(input())        # 찾을 숫자
        return cls(size, target)

# 실행부: 입력을 받아 시뮬레이션 수행 후 출력
if __name__ == "__main__":
    simulator = SnailSimulator.from_input()
    result = simulator.simulate()

    for row in result['grid']:
        print(*row)
    print(*result['position'])
