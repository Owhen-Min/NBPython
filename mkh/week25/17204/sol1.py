n, k = map(int,input().split())

dic = dict()
visited = set()

for i in range(n):
    dic[i] = int(input())

curr = 0
cnt = 0

while curr != k:
    curr = dic[curr]
    if curr in visited:
        print(-1)
        break
    cnt += 1
    visited.add(curr)

else:
    print(cnt)