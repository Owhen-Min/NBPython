def dfs(ans, value, included, visited):
    # k개를 담았다면, set에 담아서 return한다.
    if included == k:
        ans.add(value)
        return ans

    # 아니라면, 여태까지 담지 않은 애들 중에서 골라서 하나 추가로 담아본다.
    for i in range(n):
        if i not in visited:
            visited.append(i)
            dfs(ans, value+nums[i], included+1, visited)
            visited.pop()

    return ans



n = int(input())
k = int(input())
nums = list(input() for _ in range(n))
ans = dfs(set(), '', 0, [])
print(len(ans))