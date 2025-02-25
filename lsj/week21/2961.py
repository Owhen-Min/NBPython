from itertools import combinations

N = int(input())


S = 0
B = 0
ls = [tuple(map(int, input().split())) for _ in range(N)] # 재료들의 신맛, 쓴맛(S, B)으로 구성된 리스트

result = 1000000000
for i in range(1, N+1):
    for combination in combinations(ls, i):
        S = 1   # 신 맛
        B = 0   # 쓴 맛

        for s, b in combination:
            S *= s
            B += b

            if result >= abs(S - B):
                result = abs(S - B)


print(result)

