import numpy as np

def tanh_soft_cap(logits, softcap):
    """Apply tanh soft-capping to logits.

    Args:
        logits: numpy array of any shape.
        softcap: positive float, or None/<=0 to disable.

    Returns:
        numpy array of the same shape with soft-capped values,
        rounded to 6 decimal places.
    """

    if softcap is None or softcap <= 0:
        return logits
    # out = [np.round(softcap*np.tanh(i/softcap)).tolist() for i in logits]
    logits = np.array(logits)
    return np.round(softcap * np.tanh(logits / softcap), 6)
