def kaufman_roberts(rhos, b, c):
    # Calculate the amount of job classes from the length of capacity requirements
    classes = len(b)

    # Blocking probabilities for each class
    blocking_probabilities = [0] * classes

    # Initialize arrays for blocking probabilities for each class and number of busy channels
    g = [0] * c + [1] + [0] * c
    q = [0] * (c + 1)

    # Calculate probabilities of total number of busy channels
    for i in range(c + 1, 2 * c + 1):
        for j in range(classes):
            g[i] += (1 / (i - c)) * b[j] * rhos[j] * g[i - b[j]]
    normalizing_constant = sum(g)

    # Calculate probabilities for number of busy channels after normalization
    for k in range(c + 1):
        q[k] = g[k + c] / normalizing_constant

    # Calculate probabilities for each class
    for m in range(classes):
        for i in range(c):
            blocking_probabilities[m] += q[c - i] if (b[m] - 1) >= i else 0

    # Print the result
    for x, y in enumerate(blocking_probabilities):
        # print(("B{} = {}".format(x, f'{y:.10f}')))
        print(("B{} ≈".format(x).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))), "{}".format(f'{y:.10f}'))


kaufman_roberts([1, 0.14, 0.04, 0.02], [1, 3, 4, 5], 5)
