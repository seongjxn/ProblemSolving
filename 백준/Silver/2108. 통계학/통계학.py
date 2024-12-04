import sys ; input = sys.stdin.readline
from collections import Counter

N = int(input().rstrip())
Li = [int(input().rstrip()) for _ in range(N)]
Li.sort()

count = Counter(Li).most_common(2)

res = round(sum(Li) / N)
print(res)

res = Li[N // 2]
print(res)

if N > 1 :
    res = count[1][0] \
        if count[0][1] == count[1][1] \
        else count[0][0]
else :
    res = count[0][0]
print(res)  

res = max(Li) - min(Li)
print(res)