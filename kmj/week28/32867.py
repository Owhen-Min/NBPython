n, k = map(int, input().split())
keys = list(map(int, input().split()))

cnt = 0
min_key = keys[0]
max_key = keys[0]

for i in range(1, n):
    c = keys[i]
    min_key = min(min_key, c)
    max_key = max(max_key, c)

    # 손이 닿는 범위를 벗어남
    if max_key - min_key >= k:
        cnt += 1
        # 손을 옮겼으니 새 구간 시작
        min_key = c
        max_key = c

print(cnt)

"""
# 처음에 접근한 방법
min_key = keys[0]
max_key = min_key + k - 1
---
if min_key <= key <= max_key:  # 손 안에 있음
    continue
else:  # 손 밖이면 이동
    cnt += 1
    min_key = key
    max_key = key + k - 1
"""
