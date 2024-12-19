import sys ; input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
queue = deque([i + 1 for i in range(N)])
removed_number = list()

count = 1
while len(queue) :
    temp = queue.popleft()
    
    if count % K == 0 :
        removed_number.append(temp)
    else :
        queue.append(temp)
    
    count += 1

print('<', end='')
for i in range(N) :
    if i + 1 != N :
        print(f"""{removed_number[i]},""", end=' ')
    else :
        print(f"""{removed_number[i]}>""")