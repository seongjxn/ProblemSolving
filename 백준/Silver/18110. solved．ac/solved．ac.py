import sys ; input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())

def solution(n : int) :
    if not n :
        return 0
    
    Li = [int(input().rstrip()) for _ in range(n)]
    Li = deque(sorted(Li))
    
    cutoff = n * 0.15
    cutoff = int(cutoff) + 1 if cutoff % 1 >= 0.5 else int(cutoff)
    
    for _ in range(cutoff) :
        Li.popleft()
        Li.pop()
        
    res = sum(Li) / (n - cutoff * 2)
    res = int(res) + 1 if res % 1 >= 0.5 else int(res)
    
    return res
    
print(solution(n))