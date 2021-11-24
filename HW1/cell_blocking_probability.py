import math


def blocking_probability(a, b, n):
    return ((((a * b) ** n) / math.factorial(n)) / (sum((a * b) ** i / math.factorial(i) for i in range(0, n + 1))))


list = []
q15, q16 = 60, 71
f = q15

for x1 in range(1, f + 1):
    for x2 in range(1, f + 1 - x1):
        for x3 in range(1, f + 1 - x1 - x2):
            for x4 in range(1, f + 1 - x1 - x2 - x3):
                x5 = f - x1 - x2 - x3 - x4
                list.append([x1 + x4, x2 + x5, x3, x4 + x1, x5 + x2])
                list.append([x1 + x4, x2 + x5, x3, x4, x5 + x1 + x2])
                list.append([x1 + x4 + x5, x2, x3, x4, x5 + x1 + x2])
                list.append([x1 + x4 + x5, x2, x3, x4 + x1, x5 + x2])

result = 1
for i in list:
    temp = (1 - (1 - ((1 / 38) * blocking_probability(1.5, 1, i[0]))) * (
                1 - ((3 / 38) * blocking_probability(1.5, 3, i[1]))) * (
                        1 - ((7 / 38) * blocking_probability(1.5, 7, i[2]))) * (
                        1 - ((11 / 38) * blocking_probability(1.5, 11, i[3]))) * (
                        1 - ((16 / 38) * blocking_probability(1.5, 16, i[4]))))
    if temp < result:
        result = temp
        print("{}\tchannels blocking probability: {}".format(i, f'{temp:.10f}'))
