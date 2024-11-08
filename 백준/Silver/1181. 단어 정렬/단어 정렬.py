# BOJ 1181 : 단어 정렬
# https://www.acmicpc.net/problem/1181


import sys ; input = sys.stdin.readline

Li = sorted(set(input().rstrip() for _ in range(int(input().rstrip()))))

for word in sorted(Li, key=lambda x: len(x)):
    print(word) 