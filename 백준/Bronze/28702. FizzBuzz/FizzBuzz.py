import sys ; input = sys.stdin.readline

inputs = [input().rstrip() for _ in range(3)]

result = 0

for idx, i in enumerate(inputs) :
    try:
        if i.isdigit() :
            result = int(i) + (3 - idx)
            break
    except :
        pass

if result % 15 == 0 :
    print('FizzBuzz')
elif result % 3 == 0 :
    print('Fizz')
elif result % 5 == 0 :
    print('Buzz')
else :
    print(result)