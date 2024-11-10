import sys ; input = sys.stdin.readline

dp = [list(range(15)) for _ in range(15)]

for a in range(1, 15) :
    for b in range(2, 15) :
        dp[a][b] = dp[a-1][b] + dp[a][b-1]

T = int(input().rstrip())

for _ in range(T) :
    k = int(input().rstrip())
    n = int(input().rstrip())
    
    print(dp[k][n])