import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n = len(data)
    shuffeled_indices = np.random.default_rng(seed).permutation(n)
    train_end = int(n * train_frac)
    validation_end = train_end + int(validation_frac * n)

    train = data[shuffeled_indices[:train_end]]
    val = data[shuffeled_indices[train_end:validation_end]]
    test = data[shuffeled_indices[validation_end:]]
    return train, val, test