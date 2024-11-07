# BOJ 1966 : 프린터 큐
# https://www.acmicpc.net/problem/1966


import sys ; input = sys.stdin.readline

result = []

for _ in range(int(input())) :
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    
    q_idx = [i for i in range(N)]
    q_sorted = sorted(q, reverse=True)
    
    i = 0
    while i <= N :
        if q == q_sorted :
            break
        
        if q_sorted[i] > q[i] :
            q.append(q.pop(i))
            q_idx.append(q_idx.pop(i))
        
        if q[i] == q_sorted[i]:
            i += 1
    
    result.append(q_idx.index(M) + 1)

for r in result :
    print(r)