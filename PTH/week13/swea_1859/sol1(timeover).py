'''
<백만 장자 프로젝트>
- 처음 생각 난 알고리즘
인풋 받은 값들을 순서대로 본다.
해당 날의 순서가 왔을 때 상품을 구매할지 말지를 결정한다. 어떻게???

if 뒤에 남은 값들중에 오늘의 값보다 비싼날이있다?:
    사!
else:
    사지마!

그렇다면 산 녀석들은 언제 팔아야하나???
뒤에 오는 값들중에 가장 값이 큰날 ( 가장 비싸게 팔수 있는날 )

6개까지 통과 나머지 시간초과
'''
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_margin = 0
    # print(f'#{tc} {N} {arr}')

    for idx in range(N):
        margin = 0
        if arr[idx] == max(arr[idx:]):
            continue
        else:  # 사는거지. 그럼 언제 팔까?
            margin -= arr[idx]
            margin += max(arr[idx + 1:])
        if margin != 0:
            total_margin += margin

    print(f'#{tc} {total_margin}')
