import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_margin = 0

    # 미래의 최댓값을 기록할 변수를 초기화
    max_future_price = arr[-1]

    # 배열을 뒤에서부터 탐색
    for idx in range(N - 2, -1, -1):
        # 만약 현재 값이 미래의 최댓값보다 작다면 이익 발생
        if arr[idx] < max_future_price:
            total_margin += max_future_price - arr[idx]
        # 미래의 최댓값을 업데이트
        else:
            max_future_price = arr[idx]

    print(f'#{tc} {total_margin}')
