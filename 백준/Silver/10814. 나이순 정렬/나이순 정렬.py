# BOJ 10814 : 나이순 정렬
# https://www.acmicpc.net/problem/10814


import sys ; input = sys.stdin.readline

Li = [(input().rstrip().split()) for _ in range(int(input().rstrip()))]

for item in sorted(Li, key=lambda x: int(x[0])) :
    print(f"{item[0]} {item[1]}")