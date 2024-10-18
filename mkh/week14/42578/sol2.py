from collections import Counter
from functools import reduce


def solution(clothes):
    A = Counter([kind for _, kind in clothes])
    ans = reduce(lambda x, y: x*(y+1), A.values(), 1)
    return ans -1


