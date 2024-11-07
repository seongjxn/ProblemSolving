# BOJ 10989 : 수 정렬하기 3
# https://www.acmicpc.net/problem/10989


import sys ; input = sys.stdin.readline

N = int(input())
arr = [0] * 10001

for _ in range(N) :
    arr[int(input())] += 1

for i in range(10001) :
    for _ in range(arr[i]) :
        print(i)