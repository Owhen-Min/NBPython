dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(n: int, find_n: int) -> dict:
    grid = [[0 for _ in range(n)] for _ in range(n)]
    y, x = n // 2, n // 2
    position = [y + 1, x + 1]
    grid[y][x] = 1
    cur_num, cur_step = 2, 1
    while cur_num <= n * n:
        for direction in range(4):
            for _ in range(cur_step):
                if cur_num > n * n:
                    break
                y += dy[direction]
                x += dx[direction]

                if 0 <= x < n and 0 <= y < n:
                    if cur_num == find_n:
                        position = [y + 1, x + 1]
                    grid[y][x] = cur_num
                    cur_num += 1
                    if cur_num > n * n:
                        break
            if direction % 2 == 1:
                cur_step += 1

            if cur_num > n * n:
                break

    return {'grid': grid, 'position': position}

# 실행부
if __name__ == "__main__":
    number = int(input()) # 홀수인 자연수
    find_number = int(input()) # 찾는 자연수
    result = solution(n = number, find_n = find_number)

    for key, val in result.items():
        if key == 'grid':
            for li in val:
                print(*li)
        else:
            print(*val)
