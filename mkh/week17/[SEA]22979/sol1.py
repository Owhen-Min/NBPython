for _ in range(int(input())):
    s = input()
    l = len(s)
    n = int(input())
    com = sum(map(int,input().split()))%l
    print(s[com:]+s[:com])