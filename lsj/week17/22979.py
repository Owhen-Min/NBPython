import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    word = input()
    K = int(input())
    num_li = list(map(int, input().split()))
    num_sum = sum(num_li)

    if num_sum > 0:
        result_num = num_sum % len(word)
        print(word[result_num:] + word[0:result_num])

    elif num_sum < 0:
        result_num =abs(num_sum) % len(word)
        print(word[-result_num:] + word[0:-result_num])


    else:
        print(word)



