# BOJ 2751 : 수 정렬하기 2
# https://www.acmicpc.net/problem/2751


import sys ; input = sys.stdin.readline

Li = sorted([int(input().rstrip()) for _ in range(int(input().rstrip()))])

for num in Li:
    print(num)