from itertools import permutations

n = int(input())

anss = permutations(map(str,range(1, n+1)))

for ans in anss:
    print(' '.join(ans))