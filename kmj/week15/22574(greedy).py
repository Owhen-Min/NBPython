# 그렇구나... 폭탄이 1개니까 걍 쭉 오르되, 폭탄이 존재하면 1층에서만 멈추면 되는구나.....

T = int(input())
for tc in range(1, T+1):
    N, P = map(int,input().split())

    max_floor = 0 # 갈 수 있는 가장 높은 층
    flog = False

    for i in range(1, N+1):
        max_floor += i  # 층 오르기
        if max_floor == P : # 폭탄있는 층에 도착한다면
            flog = True # 폭탄있는 층 피하기 위해 1층에서는 멈춤 => 나중에 -1 해주기위한 플래그

    if flog: # 폭탄있는 층 도착한다면 피하기 위해 1층에서는 멈추기
        max_floor -= 1

    print(max_floor)

