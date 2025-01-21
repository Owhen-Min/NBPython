n = int(input())

for _ in range(n):
    cnt = 0
    ans = "NO"
    s = input()
    for c in s:
        if c == "(":
            cnt += 1    
        else:
            cnt -= 1
        if cnt <0:
            break
    else:
        if not cnt: ans = "YES"
    print(ans)