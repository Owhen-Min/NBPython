# A를 K로 만들기
from collections import deque

def min_oper(A, K):
    queue = deque([(A, 0)])  # (현재 값, 연산 횟수)
    visited = set()  # 방문한 값 (중복 반복 막기)
    
    while queue:
        v, s = queue.popleft() # (값, 몇 단계인가)
        
        if v == K:
            return s
        
        # 연산 1: +1
        if v + 1 <= K and v + 1 not in visited:
            queue.append((v + 1, s + 1))
            visited.add(value + 1) # 계산
        
        # 연산 2: *2
        if v * 2 <= K and v * 2 not in visited:
            queue.append((v * 2, s + 1))
            visited.add(v * 2) # 계산


A, K = map(int, input().split())

print(min_oper(A, K))
