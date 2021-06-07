def min_max_normalizer(x):
    if x is None:
        x = 0
    min = 0
    max = 2000
    range = max - min
    return [(a - min) / range for a in x]
