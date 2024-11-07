# BOJ 30802 : 웰컴 키트 
# https://www.acmicpc.net/problem/30802


import sys ; input = sys.stdin.readline

N = int(input().rstrip())
shirt = map(int, input().split())
T, P = map(int, input().split())

T_pack = 0

for s in shirt :
    if not s : continue
    val = s / T
    T_pack += int(val + 1 if val > int(val) else val)

print(T_pack)
print(N // P, N % P)