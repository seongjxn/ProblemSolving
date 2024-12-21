import sys ; input = sys.stdin.readline

N, M = map(int, input().split())

no_hears = set([input().rstrip() for _ in range(N)])

no_hear_seens = list()

for _ in range(M) :
    no_seen = input().rstrip()
    
    if no_seen in no_hears :
        no_hear_seens.append(no_seen)
        
no_hear_seens = sorted(no_hear_seens)

print(len(no_hear_seens))
for no_hear_seen in no_hear_seens :
    print(no_hear_seen)