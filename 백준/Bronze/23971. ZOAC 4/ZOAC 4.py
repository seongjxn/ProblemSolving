import sys ; input = sys.stdin.readline
import math

H, W, N, M = map(int, input().split())

rows = math.ceil(H / (N + 1))
cols = math.ceil(W / (M + 1))

print(rows * cols)