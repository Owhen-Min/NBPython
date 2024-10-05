'''
어라 시간초과!!! 어디서?

max()를 너무 자주 계산하나??? max()를 최대한 줄여보자

7개까지 통과 나머지 시간초과
'''

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_margin = 0
    sorted_arr = sorted(arr) # max() 사용을 줄이기 위해 미리 정렬해두자

    for idx in range(N):
        margin = 0
        sorted_arr.remove(arr[idx])
        if len(sorted_arr) > 0:
            if arr[idx] >= sorted_arr[-1]:
                continue
            else:
                margin -= arr[idx]
                margin += sorted_arr[-1]
            total_margin += margin

    print(f'#{tc} {total_margin}')