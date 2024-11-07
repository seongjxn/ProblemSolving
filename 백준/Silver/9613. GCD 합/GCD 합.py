# BOJ 9613 : GCD 합
# https://www.acmicpc.net/problem/9613


import sys ; input = sys.stdin.readline

t = int(input())
result = []

def func_GCD(a, b) :    
    if c:= a % b :
        return func_GCD(b, c)
    return b

for _ in range(t) :
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    
    gcds = []
    for i in range(n) :
        for j in range(n) :
            if i == j :
                break
            gcds.append(func_GCD(nums[i], nums[j]))
            
    result.append(sum(gcds))

for res in result :
    print(res)