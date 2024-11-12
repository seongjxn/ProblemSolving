import sys ; input = sys.stdin.readline

A, B, V = map(int, input().split())

days = (V - A) // (A - B) + 1
if (V - A) % (A - B) : days += 1

print(days)