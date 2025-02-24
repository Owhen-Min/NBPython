from itertools import combinations
l, c = map(int,input().split())
print('\n'.join([''.join(poss) for poss in combinations(sorted(input().split()), l) if any(char in {'a', 'e', 'i', 'o', 'u'} for char in poss) and sum(1 for char in poss if char not in {'a', 'e', 'i','o', 'u'})>=2]))