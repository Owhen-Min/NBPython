T = int(input())
for tc in range(T):
    N, P = map(int,input().split())
    h = 0
    for i in range(1,N+1):
        h += i
        if h == P:
            h -=1
    print(h)