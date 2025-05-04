import argparse

from src.data_fetching import fetch_stock_data
from src.indicators import compute_momentum
from src.visualization import plot_close_and_momentum
from src.strategy import apply_momentum_strategy
from src.visualization import plot_strategy_vs_buy_hold


if __name__ == "__main__": #This line ensures that the code inside the block only runs when the file is executed directly, not when it’s imported as a module.
    
    parser = argparse.ArgumentParser(description="Momentum strategy plotter")
    parser.add_argument("--window", type=int, default=10, help="Window size for momentum calculation")
    parser.add_argument("--ticker", type=str, default="AAPL", help="Ticker of the stock")
    parser.add_argument("--start", type=str, default= "2019-01-01", help="Start date for momentum calculation")
    parser.add_argument("--end", type=str, default= "2022-01-01", help="Start date for momentum calculation")
    args = parser.parse_args()
    window = args.window
    ticker = args.ticker
    start = args.start
    end = args.end
    
    # Example usage
    df = fetch_stock_data(ticker, start, end)
    print(df.head())
    df = compute_momentum(df, window)
    plot_close_and_momentum(df, ticker)

    # Apply strategy
    data = apply_momentum_strategy(df)

    # Plot strategy vs buy-and-hold
    plot_strategy_vs_buy_hold(data, ticker)
