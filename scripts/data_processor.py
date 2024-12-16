import pandas as pd
def process_stock_data(stock_data):

    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.set_index('Date', inplace=True)

    # Ensure numeric columns are properly formatted
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    stock_data[numeric_cols] = stock_data[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Drop rows with missing data
    stock_data.dropna(inplace=True)

    # Moving Averages (50-day and 200-day)
    stock_data['MA50'] = stock_data['Adj Close'].rolling(window=50).mean()
    stock_data['MA200'] = stock_data['Adj Close'].rolling(window=200).mean()

    # Bollinger Bands
    stock_data['Rolling_Mean'] = stock_data['Adj Close'].rolling(window=20).mean()
    stock_data['Rolling_Std'] = stock_data['Adj Close'].rolling(window=20).std()
    stock_data['Upper_Band'] = stock_data['Rolling_Mean'] + (2 * stock_data['Rolling_Std'])
    stock_data['Lower_Band'] = stock_data['Rolling_Mean'] - (2 * stock_data['Rolling_Std'])

    # Relative Strength Index (RSI)
    delta = stock_data['Adj Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    stock_data['RSI'] = 100 - (100 / (1 + rs))

    return stock_data