
import matplotlib.pyplot as plt


def plot_stock_data(stock_data, company_name):
    # Plot Adjusted Close with Moving Averages
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Adj Close'], label='Adj Close', color='blue')
    plt.plot(stock_data['MA50'], label='50-Day MA', color='orange', linestyle='--')
    plt.plot(stock_data['MA200'], label='200-Day MA', color='green', linestyle='--')
    plt.title(f'{company_name} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot Bollinger Bands
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Adj Close'], label='Adj Close', color='blue')
    plt.plot(stock_data['Upper_Band'], label='Upper Bollinger Band', color='red', linestyle='--')
    plt.plot(stock_data['Lower_Band'], label='Lower Bollinger Band', color='green', linestyle='--')
    plt.title(f'{company_name} Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 4))
    plt.plot(stock_data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f'{company_name} Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.grid()
    plt.show()
