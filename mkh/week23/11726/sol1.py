n=int(input())
dp=[0]*n

try:
    dp[0]= 1
    dp[1]= 2
except:
    pass
    
for i in range(2,n):
    dp[i]=(dp[i-1]+dp[i-2])%10007
    
print(dp[n-1])