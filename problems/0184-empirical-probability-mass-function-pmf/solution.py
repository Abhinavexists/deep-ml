def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function

    map = {}
    for i in samples:
        map[i] = map.get(i, 0) + 1

    new_map = [(x, count / len(samples)) for x, count in map.items()]
    return new_map