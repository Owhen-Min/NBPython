# 4 6
# a t c i s w

# l, c가 들어오는데 c개의 글자 중에서 l개를 골라서 만들 수 있는 글자수 조합 구하기. c개의 글자는 다음 줄에 들어온다.
# 단 1. 정렬이 되어있어야 하며, 2. 1개 이상의 모음과 2개 이상의 자음이 있어야 함.
# 모음의 개수가 5개로 압도적으로 적으므로, 모음의 수로 체크하는게 편하다.
from itertools import combinations

l, c = map(int,input().split())
ls = sorted(input().split())

# 처음에 sorted로 정렬한 다음에 고르기 시작하면 그 결과물은 자연스럽게 사전순으로 나오므로 딱히 정렬할 필요가 없게 됨.

combs = combinations(ls, l)

vowels = {'a', 'e', 'i', 'o', 'u'}

for comb in combs:
    consonant = 0
    vowel = 0
    for char in comb:
        if char in vowels:
            vowel += 1
        else:
            consonant += 1
    if vowel > 0 and consonant > 1:
        print(''.join(comb))