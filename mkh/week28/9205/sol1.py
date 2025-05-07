from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int,input().split()))
    stack = deque([start]) 
    visited = set([start])
    convenient_stores = [tuple(map(int,input().split())) for _ in range(n)]
    end_x, end_y = map(int,input().split())
    ans = "sad"

    while stack:
        curr_x, curr_y = stack.pop()
        if abs(end_x-curr_x) + abs(end_y-curr_y) <= 1000: 
            ans = "happy"
            break
        
        for next_x, next_y in convenient_stores:
            if (next_x, next_y) not in visited and abs(next_x-curr_x) + abs(next_y-curr_y) <= 1000:
                stack.append((next_x, next_y))
                visited.add((next_x, next_y))

    print(ans)