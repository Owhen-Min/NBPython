'''
3
2 2
2 1
10 10000

'''
T = int(input())
for tc in range(1, T + 1):
    _ = list(map(int, input().split()))
    N = _[0]
    P = _[1]
    current_floor = 0
    for i in range(1, N + 1):
        if current_floor + i != P:
            current_floor += i
        else:
            continue
    print(current_floor)


T = int(input())
for tc in range(1, T + 1):
    _ = list(map(int, input().split()))
    N = _[0]
    P = _[1]
    current_floor = 0
    for i in range(1, N + 1):
        current_floor += i
        if current_floor == P:
            current_floor -= 1
    print(current_floor)