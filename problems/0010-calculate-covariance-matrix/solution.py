def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    m = len(vectors)      # number of variables
    n = len(vectors[0])   # number of observations

    means = [sum(row) / n for row in vectors]

    cov = [[0.0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            s = 0
            for k in range(n):
                s += (
                    (vectors[i][k] - means[i])
                    * (vectors[j][k] - means[j])
                )
            cov[i][j] = s / (n - 1)

    return cov