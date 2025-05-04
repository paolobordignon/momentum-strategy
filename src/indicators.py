import pandas as pd

def compute_momentum(data: pd.DataFrame, window: int = 10) -> pd.DataFrame:
    """
    Compute simple momentum as the difference between the current Close and the Close 'window' days ago.

    Args:
        data (pd.DataFrame): DataFrame containing stock data with a 'Close' column.
        window (int): Number of days for momentum calculation.

    Returns:
        pd.DataFrame: Updated DataFrame with a new 'Momentum' column.
    """
    data["Momentum"] = data["Close"] - data["Close"].shift(window)
    return data