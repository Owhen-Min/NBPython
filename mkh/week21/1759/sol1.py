from itertools import permutations

l, c = map(int,input().split())

print('\n'.join([''.join(poss) for poss in permutations(sorted(input().split()), l)]))