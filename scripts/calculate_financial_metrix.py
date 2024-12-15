

import numpy as np


def calculate_financial_metrics(stock_data):
    # Calculate daily returns
    returns = stock_data['Adj Close'].pct_change().dropna()

    # Calculate Sharpe Ratio (assuming a risk-free rate of 0)
    mean_return = returns.mean()
    std_dev = returns.std()
    sharpe_ratio = mean_return / std_dev

    # Calculate Annualized Return (assuming 252 trading days in a year)
    annualized_return = (1 + mean_return)**252 - 1

    # Calculate Annualized Volatility
    annualized_volatility = std_dev * np.sqrt(252)

    return sharpe_ratio, annualized_return, annualized_volatility
