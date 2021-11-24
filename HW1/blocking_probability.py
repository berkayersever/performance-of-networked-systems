import math


def blocking_probability(n):
    print("{}\tchannels blocking probability: {}".format(n, f'{(1 / math.factorial(n)) / (sum(1 / math.factorial(i) for i in range(0, n + 1))):.20f}'))


blocking_probability(5)
blocking_probability(10)
