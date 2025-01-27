n, s = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0

for i in range(1, 1<<n):
    value = 0
    # 값들이 들어간 모든 경우의 수를 bitmasking을 통해서 뽑는다.
    for index, v in enumerate(nums):
        if (1<<index) & i:
            value += v
    if value == s:
        ans +=1

print(ans)