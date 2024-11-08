# BOJ 2870 : 수학숙제
# https://www.acmicpc.net/problem/2870


import sys ; input = sys.stdin.readline
import re

Li = []
for _ in range(int(input().rstrip())):
    Li += re.split('[a-z]', input().rstrip())
    
Li = sorted([int(v) for v in Li if v])
for num in Li:
    print(num)