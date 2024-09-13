import sys
sys.stdin = open('input.txt', 'r')
'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''


def cal_K_under_subset(start_idx=0, current=[], total_cal=0):
    global max_score
    if start_idx == len(matrix):
        if total_cal <= limit:
            # print(current)
            current_cal = 0
            for i in range(len(current)):
                current_cal += current[i][0]
            if max_score < current_cal:
                max_score = current_cal
        return

    # 포함하지 않은 경우
    cal_K_under_subset(start_idx + 1, current, total_cal)

    # 포함한 경우
    current.append(matrix[start_idx])
    cal_K_under_subset(start_idx + 1, current, total_cal + matrix[start_idx][1])
    current.pop()


T = int(input())
for tc in range(1, T + 1):
    N, limit = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    max_score = 0
    cal_K_under_subset()
    print(f'#{tc} {max_score}')
