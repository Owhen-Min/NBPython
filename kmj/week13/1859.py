import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    D = int(input())  # day
    D_bargain = list(map(int, input().split()))  # day별 매매값

    max_bargain = 0  # 최대 이익..최종 결과
    max_price = 0  # 현재까지 찾은 날 중 매매가 최대인 날의 매매가

    # day를 뒤부터 순회
    for i in range(D - 1, -1, -1):
        # 매매가 최대인 날을 찾으면 갱신
        if D_bargain[i] > max_price:
            max_price = D_bargain[i]
        else:
            max_bargain += (max_price - D_bargain[i]) # 찾지 못한 날은 팔기

    print(f'#{tc} {max_bargain}')
