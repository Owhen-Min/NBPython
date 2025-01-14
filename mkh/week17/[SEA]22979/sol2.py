from collections import deque
 
t = int(input())
for tc in range(t):
    s = deque(input())
    n = int(input())
    com = sum(map(int,input().split()))%len(s)
    s.rotate(-com)
    print(''.join(s))