import numpy as np
from app.portfolio import Portfolio

def test_expected_return():
    returns = np.array([
        [0.01, 0.02, -0.01],
        [-0.02, 0.03, 0.01],
        [0.03, -0.01, 0.02]
    ])

    weights = [0.4, 0.4, 0.2]

    portfolio = Portfolio(weights, returns)
    expected = np.sum(returns.mean(axis=0) * weights)
    assert np.isclose(portfolio.expected_return(), expected)

def test_risk():
    returns = np.array([
        [0.01, 0.02, -0.01],
        [-0.02, 0.03, 0.01],
        [0.03, -0.01, 0.02]
    ])

    weights = [0.4, 0.4, 0.2]

    portfolio = Portfolio(weights, returns)
    cov_matrix = np.cov(returns.T)
    expected = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    assert np.isclose(portfolio.risk(), expected)

def test_sharpe_ratio():
    returns = np.array([
        [0.01, 0.02, -0.01],
        [-0.02, 0.03, 0.01],
        [0.03, -0.01, 0.02]
    ])

    weights = [0.4, 0.4, 0.2]
    risk_free_rate = 0.02

    portfolio = Portfolio(weights, returns)
    expected_return = np.sum(returns.mean(axis=0) * weights)
    cov_matrix = np.cov(returns.T)
    risk = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    expected_sharpe_ratio = (expected_return - risk_free_rate) / risk

    assert np.isclose(portfolio.sharpe_ratio(risk_free_rate), expected_sharpe_ratio)
