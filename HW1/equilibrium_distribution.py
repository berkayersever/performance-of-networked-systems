import math

states = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0], [5, 0, 0, 0],
          [0, 0, 0, 1], [0, 1, 0, 0], [1, 1, 0, 0], [2, 1, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0]]
rhos = [1, 0.14, 0.04, 0.02]


def normalizing_constant(states, rhos):
    sum = 0
    for state in states:
        partial_sum = 1
        for i, j in enumerate(state):
            partial_sum *= (rhos[i] ** j) / math.factorial(j)
        sum += partial_sum
    return sum


def equilibrium_distribution(states, rhos):
    g = normalizing_constant(states, rhos)
    result = {}
    for x, state in enumerate(states):
        sum = 1
        for n, m in enumerate(state):
            sum *= (rhos[n] ** m) / math.factorial(m)
        sum *= (1 / g)
        result[x] = (state, sum)
    return result


result = equilibrium_distribution(states, rhos)

for value in result.values():
    print("\u03C0{} : {}".format(value[0], f'{value[1]:.10f}'))
