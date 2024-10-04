def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            answer.append(-1)
        elif numbers[i] == 1000000:
            answer.append(-1)
            break    

        else:
            for j in range(i + 1, len(numbers)):
                if numbers[i] < numbers[j]:
                    answer.append(numbers[j])
                    break
            else:
                answer.append(-1)

    return answer