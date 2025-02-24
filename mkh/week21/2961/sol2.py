n = int(input())
ingreds = [list(map(int,input().split())) for _ in range(n)]

def dfs(depth, sour, bitter):
    if depth == n:
        if (sour != 1 and bitter != 0):
            return abs(sour-bitter)
        return 10e9
    
    return min(dfs(depth+1, sour*ingreds[depth][0], bitter+ingreds[depth][1]), dfs(depth+1, sour, bitter))

ans = dfs(0,1,0)

print(ans)