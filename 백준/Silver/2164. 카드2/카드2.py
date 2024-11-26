import sys ; input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

cards = deque([i + 1 for i in range(N)])

while len(cards) > 1 :
    cards.popleft()
    i = cards.popleft()
    cards.append(i)

print(cards[0])