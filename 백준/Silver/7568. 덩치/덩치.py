# BOJ 7568 : 덩치
# https://www.acmicpc.net/problem/7568


import sys ; input = sys.stdin.readline

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

rank_list = [0 for _ in range(N)]

rank = N
count = 0
for i in range(N) :
    for j in range(N) :
        if i == j :
            continue
        
        if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
            rank_list[i] += 1
        
for i in range(N) :
    rank = rank_list[i]
    print(rank + 1, end=" ")