from collections import defaultdict, deque
def main(n, m, v):
    node = defaultdict(list)
    for _ in range(m):
        s, e = map(int, input().split())
        node[s].append(e)
        node[e].append(s)

    stack = [v]
    queue = deque([v])

    visited1 = set()
    visited2 = set()

    while stack:
        temp = stack.pop()


n, m, v = map(int, input().split())