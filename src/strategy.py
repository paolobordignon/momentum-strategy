import pandas as pd

def apply_momentum_strategy(data: pd.DataFrame) -> pd.DataFrame:
    """
    Apply a simple momentum-based trading strategy:
    - Go long (position = 1) when momentum > 0
    - Stay out (position = 0) when momentum <= 0

    Returns:
        pd.DataFrame with added columns: Position, Strategy_Returns, Cumulative_Returns
    """
    data = data.copy()

    # Define position: long if momentum > 0
    data["Position"] = (data["Momentum"] > 0).astype(int)

    # Daily returns of the asset
    data["Returns"] = data["Close"].pct_change()

    # Strategy return = asset return * position taken
    data["Strategy_Returns"] = data["Returns"] * data["Position"].shift(1)  # use .shift(1) to avoid look-ahead bias

    # Cumulative return of the strategy
    data["Cumulative_Strategy"] = (1 + data["Strategy_Returns"]).cumprod()
    data["Cumulative_Buy_Hold"] = (1 + data["Returns"]).cumprod()

    return data