# union find 방식으로 찾기

# 가리키는 부모노드가 자신이 아니라면, 더 깊이 재귀적으로 탐색하여 루트 노드를 확인한다.
def find(x):
    if mothers[x] != x:
        return find(mothers[x])
    return x

# 서로 가리키는 부모노드가 다르다면, 하나로 통합시킨다. => 부모를 하나로 만든다.
def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        mothers[rootX] = rootY

n = int(input())
e = int(input())
# 자기 자신을 부모로 가지고 있는 노드들을 만든다.
mothers = [i for i in range(n+1)]

for i in range(e):
    n1, n2 = map(int,input().split())
    union(n1, n2)


for i in range(1, n+1):
    mothers[i] = find(i)

print(sum(1 for num in mothers if num == mothers[1])-1)