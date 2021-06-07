def min_max_normalizer(x):
    if x is None:
        x = 0
    min = -1
    max = 2000
    return (x - min) / max - min
