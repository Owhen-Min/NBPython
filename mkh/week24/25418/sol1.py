from collections import deque


def bfs(a, k):
    queue = deque([(a, 0)])
    visited = set()

    while queue:
        current, count = queue.popleft()

        if current == k:  # 목표값 도달
            return count

        # +1 연산
        if current + 1 <= k and current + 1 not in visited:
            visited.add(current + 1)
            queue.append((current + 1, count + 1))

        # ×2 연산
        if current * 2 <= k and current * 2 not in visited:
            visited.add(current * 2)
            queue.append((current * 2, count + 1))


A, K = map(int, input().split())
print(bfs(A, K))
