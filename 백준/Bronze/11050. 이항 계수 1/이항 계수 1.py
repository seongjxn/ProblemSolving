# BOJ 11050 : 이항 계수 1
# https://www.acmicpc.net/problem/11050


import sys ; input = sys.stdin.readline

N, K = map(int, input().split())

nume = 1
for i in range(N, K, -1) :
    nume *= i

deno = 1
for i in range(N - K, 0, -1) :
    deno *= i

print(int(nume / deno))
