# BOJ 1271 : 엄청난 부자2
# https://www.acmicpc.net/problem/1271


import sys
n, m = map(int, sys.stdin.readline().split())

print(n // m)
print(n % m)