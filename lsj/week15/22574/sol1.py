T = int(input())
for tc in range (1, T+1):
    N, P = map(int, input().split())
    floor = 0
    for i in range(1, N+1):
        if floor + i == P:
            floor += i-1
        else:
            floor += i
    print(floor)