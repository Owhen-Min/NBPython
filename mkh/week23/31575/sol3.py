n, m = map(int,input().split())
poss_ways = set()
poss_ways.add((0,0))

for i in range(m):
    ls = input().split()
    for j in range(n):
        if ls[j]=='1' and ((i-1, j) in poss_ways or (i, j-1) in poss_ways):
            poss_ways.add((i,j,))

print('Yes') if (m-1,n-1) in poss_ways else print('No')