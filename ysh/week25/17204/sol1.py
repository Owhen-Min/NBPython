def main(n, k):
    player = dict()
    for i in range(n):
        player[i] = int(input())

    visited = set()
    cnt = 0
    next_player = 0
    while True:
        cnt += 1
        next_player = player[next_player]
        if next_player == k:
            return cnt

        if next_player in visited:
            return -1
        visited.add(next_player)

n, k = map(int, input().split())
result = main(n, k)

print(result)