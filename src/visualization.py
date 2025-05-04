import matplotlib.pyplot as plt
import pandas as pd

def plot_close_and_momentum(data: pd.DataFrame, ticker: str):
    """
    Plot closing price and momentum indicator.

    Args:
        data (pd.DataFrame): Stock data with 'Close' and 'Momentum' columns.
        ticker (str): Ticker symbol for title.
    """
    plt.figure(figsize=(14, 6))

    # Plot closing price
    plt.subplot(2, 1, 1)    # This divides the window in two rows allowing to subplot graphs
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.title(f"{ticker} - Closing Price")
    plt.ylabel('Price')
    plt.grid(True)

    # Plot momentum
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['Momentum'], label='Momentum', color='orange')
    plt.axhline(0, linestyle='--', color='gray', linewidth=1)
    plt.title(f"{ticker} - Momentum Indicator")
    plt.ylabel('Momentum')
    plt.xlabel('Date')
    plt.grid(True)

    plt.tight_layout()
    plt.show()