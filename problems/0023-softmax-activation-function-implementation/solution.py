import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here

    # o(N) time and space complexity
    # summation  = sum(math.exp(i) for i in scores)

    # need to introduce numerical stability
    max_score = max(scores)
    summation = sum(math.exp(i-max_score) for i in scores)

    return [math.exp(i-max_score)/summation for i in scores]