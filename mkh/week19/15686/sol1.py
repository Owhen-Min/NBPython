import sys
from itertools import combinations

# 특정 집에서 선택된 치킨집 조합까지의 최소 거리 계산 함수
def cal_dist(house, combi):
    y, x = house
    # 선택된 치킨집 조합 중 최소 맨해튼 거리 반환
    return min(abs(y - i) + abs(x - j) for i, j in combi)

# n: 도시 크기, m: 선택할 치킨집 개수
n, m = map(int, input().split())

# 도시 정보 입력
board = [list(sys.stdin.readline().split()) for _ in range(n)]

# 집과 치킨집의 위치 저장
house_positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == '1']
chick_positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == '2']

# 최소 도시 치킨 거리 초기화 (최대값으로 설정)
ans = 1e9

# 가능한 m개의 치킨집 조합을 순회
for combi in combinations(chick_positions, m):
    dists = 0  # 현재 조합에 대한 총 치킨 거리
    # 각 집에 대해 최소 치킨 거리 계산 후 합산
    for house in house_positions:
        dists += cal_dist(house, combi)
    # 최소 치킨 거리 갱신
    if ans > dists:
        ans = dists

# 최소 도시 치킨 거리 출력
print(ans)