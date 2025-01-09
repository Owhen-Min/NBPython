# rotate(음수 -> 반시계 회전 / 양수 -> 시계 회전)
from collections import deque

T = int(input())

for tc in range(1,T+1):
    # S = deque(input().strip())
    S = list(map(str, input())) # abcde -> ['a', 'b', 'c', 'd', 'e']
    K = int(input()) # 연산 횟수 = len(x_list)
    x_list = list(map(int, input().split()))

    q = deque(S) # deque 객체

    for x in range(K):
        X = x_list[x]
        if X > 0:
            q.rotate(-X) # 음수 -> 반시계 회전
        elif X < 0:
            q.rotate(X) # 양수 -> 시계 회전
    ##
    # for X in x_list:
    #     q.rotate(-X)  # 양수면 시계, 음수면 반시계 방향 회전

    result = list(q)
    print(''.join(result))
