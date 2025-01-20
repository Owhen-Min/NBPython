N, M = map(int, input().split())
num = list(map(int, input().split()))

num_ls = list(range(1, N + 1))
count = 0

for target in num:
    # 목표 숫자의 현재 인덱스 확인
    target_idx = num_ls.index(target)

    # 왼쪽과 오른쪽을 비교해서 최소 이동 횟수 더하기
    left_move = target_idx
    right_move = len(num_ls) - target_idx
    count += min(left_move, right_move)

    # 1번 연산 후 num_ls 갱신
    # 왼쪽 이동 경우
    if left_move <= right_move:
        num_ls = num_ls[left_move:] + num_ls[:left_move]
    # 오른쪽 이동
    else:
        num_ls = num_ls[-right_move:] + num_ls[:-right_move]

    # 1번연산(첫번째 원소 뽑아내기)
    num_ls.pop(0)

print(count)
