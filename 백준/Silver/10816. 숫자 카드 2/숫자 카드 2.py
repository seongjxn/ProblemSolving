import sys ; input = sys.stdin.readline

N = int(input().rstrip())
cards = list(map(int, input().split()))

M = int(input().rstrip())
numbers = list(map(int, input().split()))

counts = dict()

for card in cards :
    try :
        counts[card] += 1
    except KeyError :
        counts[card] = 1
    
for number in numbers :
    try :
        print(counts[number], end=' ')
    except :
        print(0, end=' ')

print()