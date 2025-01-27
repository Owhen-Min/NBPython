# 재귀로 들어가면서 모든 경우의 수를 구해주는 함수. 모든 경우의 수에 대해서 합이 s와 같다면 1을 리턴하여 정답을 도출한다.
def dfs(ls, value = 0, depth = 0):
    if depth == n:
        return 1 if value == s else 0
    return dfs(ls, value+ls[depth], depth+1) + dfs(ls, value, depth+1)


n, s = map(int,input().split())
nums = list(map(int,input().split()))
ans = dfs(nums)

# 아무것도 들어가 있지 않은 공집합도 포함하므로 s가 0일 경우 1개가 추가로 카운트된다. 따라서 -1을 해준다.
if s == 0:
    ans -= 1

print(ans)