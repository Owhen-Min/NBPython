def recur(level, sum):
    global cnt
    if sum == K:
        cnt +=1
        return

    if level == N-1:
        return


    for i in range(level,len(arr)):
        if visited[i] == 0:
            ls.append(arr[i])
            visited[i] =1
            recur(level+1, sum + arr[i])
            visited[i] = 0
            ls.pop()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    ls = []
    visited = [0] * N
    recur(0,0)
    print(f'#{tc} {cnt}')
