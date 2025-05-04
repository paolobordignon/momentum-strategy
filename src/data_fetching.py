import yfinance as yf
import pandas as pd
from pathlib import Path

def fetch_stock_data(ticker: str, start: str, end: str, save: bool = True, folder: str = "../data") -> pd.DataFrame:
    """
    Fetch historical stock data using yfinance.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        start (str): Start date (YYYY-MM-DD).
        end (str): End date (YYYY-MM-DD).
        save (bool): Whether to save the data as CSV.
        folder (str): Folder to save the CSV file in.

    Returns:
        pd.DataFrame: Historical stock data.
    """
    print(f"Fetching data for {ticker} from {start} to {end}...")
    data = yf.download(ticker, start=start, end=end)

    if save:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
        filename = path / f"{ticker}.csv"
        data.to_csv(filename)
        print(f"Saved data to {filename}")

    return data