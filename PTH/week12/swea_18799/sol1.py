'''
3
3
1 2 3
7
3 14 1 5 9 6 535
1
999

'''

def subset(start_idx=0, current=[]):
    if start_idx == len(arr):
        if len(current) != 0:
            avg = sum(current)/len(current)
            avg_list.append(avg)
        return
    # 포함하지 않은 경우
    subset(start_idx + 1, current)

    # 포함한 경우
    current.append(arr[start_idx])
    subset(start_idx + 1, current)
    current.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    avg_list = []
    subset()
    result = sum(avg_list)/len(avg_list)
    if result.is_integer():
        print(f"#{tc} {int(result)}")
    else:
        print(f"#{tc} {result:.20f}")