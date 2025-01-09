from collections import deque

T = int(input())

for tc in range(1, T + 1):
    S = deque(input().strip())  # 문자열을 deque로 변환
    K = int(input())  # 연산 횟수
    x_list = list(map(int, input().split())) 

    for X in x_list:
        S.rotate(-X)  # 양수면 반시계, 음수면 시계 방향 회전

    result = ''.join(S)
    print(result)
