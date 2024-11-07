import sys ; input = sys.stdin.readline

def solution(N) -> bool :
    for i in range(N) :
        if sum([int(x) for x in str(i)]) + i == N :
            print(i)
            return True

if not solution(int(input().rstrip())) :
    print(0)