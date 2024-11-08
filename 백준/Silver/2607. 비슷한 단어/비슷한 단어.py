# BOJ 2607 : 비슷한 단어
# https://www.acmicpc.net/problem/2607


import sys ; input = sys.stdin.readline

first_word = list()

def do_it(word: str) -> int:
    word = list(word)
    
    compare_word = first_word[:]
    
    for _ in range(len(word)):
        w = word.pop(0)
        if w in compare_word:
            compare_word.remove(w)
        else :
            word.append(w)
    
    if (len(compare_word) >= 0 and len(compare_word) <= 1 and
        len(word) >= 0 and len(word) <= 1):
        return 1
    
    return 0

if __name__ == '__main__' :
    N = int(input().rstrip())
    first_word = list(input().rstrip())

    count = 0
    for _ in range(N - 1) :
        count += do_it(input().rstrip())

    print(count)