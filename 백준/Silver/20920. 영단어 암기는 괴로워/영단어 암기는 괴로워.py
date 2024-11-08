# BOJ 20920 : 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920


import sys ; input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
word_list = []

word_list = [input().rstrip() for _ in range(N)]

word_count = Counter(word_list)
word_list = set(word_list)
word_list = list(word_list)
word_list.sort(key= lambda x: (-word_count[x], -len(x), x))

for word in word_list :
    if len(word) < M : continue
    print(word)