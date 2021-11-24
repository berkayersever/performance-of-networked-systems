import math

states = [[0, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0], [5, 0, 0, 0],
          [0, 0, 0, 1], [0, 1, 0, 0], [1, 1, 0, 0], [2, 1, 0, 0], [0, 0, 1, 0], [1, 0, 1, 0]]
rhos = [1, 0.14, 0.04, 0.02]
capacity = [1, 3, 4, 5]
max_capacity = 5


# Calculate the normalizing constant
def normalizing_constant(states, rhos):
    sum = 0
    for state in states:
        partial_sum = 1
        for i, j in enumerate(state):
            partial_sum *= (rhos[i] ** j) / math.factorial(j)
        sum += partial_sum
    return sum


# Subset of states in which class-j calls are accepted
def state_subset(states, capacity, max_capacity):
    subset = []
    for i, j in enumerate(capacity):
        subset.append([])
        for state in states:
            sum = 0
            for k, l in enumerate(state):
                sum += capacity[k] * l
            if (sum <= (max_capacity - j)) and (state not in subset):
                subset[i].append(state)
    [print("Subset of states for class {}: {}".format(i + 1, subset)) for i, subset in enumerate(subset)]
    return (subset)


# Calculate blocking probabilities for each class
def blocking_probability(states, required_capacity, capacity, rhos):
    subsets = state_subset(states, required_capacity, capacity)
    g = normalizing_constant(states, rhos)
    for j, subset in enumerate(subsets, start=1):
        # Calculate g for class-j
        gj = normalizing_constant(subset, rhos)
        # Calculate blocking probability for class-j
        blocking_probability = 1 - (gj / g)
        print("Blocking probability for class {}: {}".format(j, f'{blocking_probability:.10f}'))


blocking_probability(states, capacity, max_capacity, rhos)
