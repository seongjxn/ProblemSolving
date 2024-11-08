# BOJ 1654 : 랜선 자르기
# https://www.acmicpc.net/problem/1654


import sys ; input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
cable_list = [int(input().rstrip()) for _ in range(K)]

def func(left, right) :
    result = 0
    
    while (left <= right) :
        mid = int((left + right) / 2)
        
        count = 0
        for cable in cable_list :
            count += cable // mid
        
        if count >= N :
            left = mid + 1
            result = max(result, mid)
        else :
            right = mid - 1
    
    return result

print(func(1, max(cable_list)))
        