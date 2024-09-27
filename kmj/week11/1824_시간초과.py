# tc 1만 처리하고 시간 초과
# >> 방문 처리를 해야할 듯?

import sys
sys.stdin = open("input.txt","r")

# 명령어에 따른 이동 방향 설정 (오른쪽, 왼쪽, 아래, 위)
dir = {
    '>': (0, 1),  # 오른쪽
    '<': (0, -1), # 왼쪽
    'v': (1, 0),  # 아래쪽
    '^': (-1, 0)  # 위쪽
}

# 이동 방향을 설정하는 함수
def direction(command, memory): # '_', '|'
    # '_'
    if command == '_':
        # 메모리가 0 -> 오른쪽(0, 1)으로 이동
        if memory == 0:
            return (0, 1)  # 오른쪽
        # 메모리가 0이 아니면 -> 왼쪽(0, -1)으로 이동
        else:
            return (0, -1)  # 왼쪽

    # '|'
    elif command == '|':
        # 메모리가 0 -> 아래쪽(1, 0)으로 이동
        if memory == 0:
            return (1, 0)  # 아래쪽
        # 메모리가 0이 아니면 -> 위쪽(-1, 0)으로 이동
        else:
            return (-1, 0)  # 위쪽

    # 명령어가 '_', '|'가 아니면 None 반환
    return None


# DFS, 스텍 사용
def move(grid, R, C):
    # 초기 상태 (위치, 방향(행, 열), 메모리 값)
    stack = [(0, 0, (0, 1), 0)]

    # 스텍이 빌 때까지 반복
    while stack:
        r, c, dir_vec, memory = stack.pop()

        cmd = grid[r][c]

        # 종료 명령어 만나면 "YES" 출력 # @
        if cmd == '@':
            return "YES"

        # 메모리 값을 변경하는 명령어 처리
        if cmd.isdigit(): # 숫자라면
            memory = int(cmd) # 메모리 갱신
        elif cmd == '+':
            memory = (memory + 1) % 16 # 더하기 전 값이 15이라면 0으로 바꾼다
        elif cmd == '-':
            memory = (memory - 1) % 16 # 빼기 전 값이 0이라면 15로 바꾼다

        # 이동 방향을 바꾸는 명령어 처리
        if cmd in dir: # 이동 방향 명령어라면
            dir_vec = dir[cmd]  # 명령어에 맞는 방향 좌표를 가져옴
        elif cmd == '?':
            # 모든 방향으로 이동할 수 있기 때문에 네 방향 모두 스택에 추가
            for new_dir_vec in dir.values():
                nr = (r + new_dir_vec[0]) % R
                nc = (c + new_dir_vec[1]) % C
                stack.append((nr, nc, new_dir_vec, memory))
            continue
        else: # '.'
            new_dir_vec = direction(cmd, memory)
            if new_dir_vec:
                dir_vec = new_dir_vec

        # 다음 위치로 이동 (격자 밖으로 나가는 경우를 처리)
        nr = (r + dir_vec[0]) % R
        nc = (c + dir_vec[1]) % C

        # 다음 상태를 스택에 추가
        stack.append((nr, nc, dir_vec, memory))

    # 종료 명령을 만나지 못하면 "NO" 출력
    return "NO"

##
T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    result = move(grid, R, C)
    print(f"#{tc} {result}")
