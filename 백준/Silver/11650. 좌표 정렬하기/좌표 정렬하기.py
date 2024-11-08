# BOJ 11650 : 좌표 정렬하기
# https://www.acmicpc.net/problem/11650


import sys ; input = sys.stdin.readline

pos = []

for _ in range(int(input().rstrip())) :
    x, y = map(int, input().rstrip().split())
    pos.append((x, y))

pos.sort(key = lambda x : (x[0], x[1]))

for xy in pos :
    print(xy[0], xy[1])