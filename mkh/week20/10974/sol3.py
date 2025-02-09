n = int(input())
numbers = tuple(map(str,range(1,n+1)))
stack = ['']

while stack:
    num = stack.pop()
    if len(num) == (2*n-1):
        print(num)
    else:
        for i in range(n, 0, -1):
            if numbers[i-1] not in num:
                stack.append((num+' '+numbers[i-1]).strip())