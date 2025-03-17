import heapq

tc = 0
deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))

while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    board = [list(map(int,input().split())) for _ in range(n)]
    distance = [[25000] * n for _ in range(n)]
    distance[0][0] = board[0][0]
    heap = [(board[0][0],(0,0))]
    while heap:
        cost, (y, x) = heapq.heappop(heap)
        if y == n-1 and x == n-1:
            print(f'Problem {tc}: {cost}')
            break
        for dy, dx in deltas:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<n:
                new_cost = cost+board[ny][nx]
                if distance[ny][nx] > new_cost :
                    distance[ny][nx] = new_cost
                    heapq.heappush(heap, (new_cost,(ny, nx)))
