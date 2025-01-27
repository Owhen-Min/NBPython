from itertools import permutations

n = int(input())
k = int(input())
nums = list(input() for _ in range(n))
ans = set()

# 순서가 보장되어 있지 않으므로 순열을 통해서 k개를 뽑은 모든 경우의 수를 만든 다음 str으로 변환하여 set에 담는다.
for perm in permutations(nums, k):
    ans.add(''.join(perm))

print(len(ans))