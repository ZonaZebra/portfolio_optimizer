import numpy as np

class Portfolio:
    def __init__(self, weights, returns):
        self.weights = np.array(weights)
        self.returns = np.array(returns)

    def expected_return(self):
        return np.sum(self.returns.mean(axis=0) * self.weights)

    def risk(self):
        cov_matrix = np.cov(self.returns.T)
        return np.sqrt(np.dot(self.weights.T, np.dot(cov_matrix, self.weights)))

    def sharpe_ratio(self, risk_free_rate=0.02):
        return (self.expected_return() - risk_free_rate) / self.risk()
