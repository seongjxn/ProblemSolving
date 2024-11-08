N = int(input())
list = [float(input()) for _ in range(N)]

for i in range(1, N) :
    if (list[i] < list[i] * list[i - 1]) :
        list[i] *= list[i - 1]

print("{:.3f}".format(max(list)))