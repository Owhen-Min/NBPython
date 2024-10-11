T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ls = list(map(int,input().split()))
    hap = 0
    # 가장 큰 숫자를 저장할 변수 l_num
    l_num = ls[n-1]
    # 뒤에서부터 볼건데
    for item in ls[::-1]:
        # 만약 내가 현재까지의 가장 큰 수보다 현재 값이 크다면 갱신한다
        if l_num < item:
            l_num = item
        # 합에 내가 팔 수 있는 최댓값에서 현재 값(사는 값)을 뺀 값을 더해준다.
        else:
            hap += l_num-item
    print(f'#{tc} {hap}')