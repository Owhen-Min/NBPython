from functools import lru_cache
import sys
sys.setrecursionlimit(200000)

pw = input()
flag = False

@lru_cache()
def dp(depth):
    global flag
    if flag:
        return 0

    if depth <= 0:
        return 1

    if pw[depth] == '0':
        if pw[depth-1] not in ('1', '2',):
            flag = True
            return 0
        else:
            return dp(depth-2)
    if pw[depth-1] == '2':
        if pw[depth] in ('1', '2', '3', '4', '5', '6',):
            return (dp(depth-2) + dp(depth-1)) % 1000000
    if pw[depth-1] == '1':
        return (dp(depth-2) + dp(depth-1)) % 1000000

    else:
        return dp(depth-1)

if pw[0] == '0':
    print(0)
else:
    print(dp(len(pw)-1))

