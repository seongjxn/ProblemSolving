import sys ; input = sys.stdin.readline

N = int(input().rstrip())
P_Li = list(map(int, input().split()))

P_Li = sorted(P_Li)

result = 0
for idx in range(N) :
    result += sum(P_Li[0:idx + 1])
    
print(result)