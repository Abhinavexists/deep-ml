import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.

    Args:
        data: List or numpy array of numerical values

    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here

    
    mean = np.mean(data)
    values, counts = np.unique(data, return_counts=True)
    mode_val = values[np.argmax(counts)]
    variance =sum((i - mean)**2 for i in data)/len(data)
    quartile_values = np.quantile(data, [0.25, 0.50, 0.75])

    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': mode_val,
        'variance': sum((i - mean)**2 for i in data)/len(data),
        'standard_deviation': np.sqrt(variance),
        '25th_percentile': quartile_values[0],
        '50th_percentile': quartile_values[1],
        '75th_percentile': quartile_values[2],
        'interquartile_range': quartile_values[2]  - quartile_values[0]
    }
    pass
