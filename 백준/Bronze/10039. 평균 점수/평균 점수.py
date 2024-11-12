import sys ; input = sys.stdin.readline

score = []
for _ in range(5):
    s = int(input().rstrip())
    
    if s < 40 :
        s = 40
    
    score.append(s)

avg_score = sum(score)/5

print(int(avg_score))