# 완탐을 하되, 백트래킹으로 폭탄있는 층 도착하면 걸러주기
# 근데 왜 Runtime error가 날까 쩝

def highest_floor(cur_n, cur_floor): # 현재까지 한 선택 수, 현재까지 오른 층
    global N, P, max_floor

    # 폭탄있는 층 가는 경우의 수 제거
    if P == cur_floor:
        return

    # 선택 끝났으므로 최대 층인지 비교 (함수 종료 조건)
    if cur_n == N:
        max_floor = max(max_floor,cur_floor)
        return

    # 다음 선택에서 엘리베이터를 가만히 두는 경우
    highest_floor(cur_n + 1, cur_floor)
    # 다음 선택에서 i층을 올리는 경우
    highest_floor(cur_n + 1, cur_floor + (cur_n + 1))


T = int(input())
for tc in range(1, T+1):
    N, P = map(int,input().split())

    max_floor = 0 # 있을 수 있는 가장 높은 층의 번호 (최종 결과)

    highest_floor(0, 0)
    print(max_floor)
