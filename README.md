# 📈 Momentum Strategy Backtester

A simple Python project to backtest a momentum-based trading strategy using historical stock data.

---

## Features

- Fetches real historical stock data using [Yahoo Finance](https://finance.yahoo.com/)
- Computes a momentum indicator over a customizable rolling window
- Visualizes both price and momentum in a dual-panel plot
- Fully configurable via command-line arguments

---

## Requirements

- Python 3.10+
- macOS with Homebrew (recommended)

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Dependencies

- `yfinance`
- `pandas`
- `matplotlib`

You can install them manually:

```bash
pip install yfinance pandas matplotlib
```

Or use:

```bash
pip install -r requirements.txt
```

with the following `requirements.txt`:

```
yfinance
pandas
matplotlib
```

---

## How to Use

Run the script from your terminal:

```bash
python main.py --ticker AAPL --start 2019-01-01 --end 2022-01-01 --window 10
```

### Available Arguments:

| Argument       | Description                            | Default        |
|----------------|----------------------------------------|----------------|
| `--ticker`     | Stock symbol (e.g. `AAPL`, `MSFT`)     | `"AAPL"`       |
| `--start`      | Start date in format `YYYY-MM-DD`      | `"2019-01-01"` |
| `--end`        | End date in format `YYYY-MM-DD`        | `"2022-01-01"` |
| `--window`     | Rolling window for momentum indicator  | `10`           |

---

## Output

Generates a two-panel plot:
- **Top:** Stock closing price
- **Bottom:** Computed momentum indicator (difference between today's close and the close N days ago)

---

## Project Structure

```
momentum-strategy/
│
├── data/                 # Saved historical CSVs
├── src/
│   ├── data/             # Data fetching and processing functions
│   └── visualization/    # Plotting functions
├── main.py               # Script entry point
├── requirements.txt
└── README.md             # Project documentation
```

---

## Future Work

This is Weekend 1 of a multi-stage project. Next steps will include:

- Adding buy/sell signal generation
- Backtesting the strategy over time
- Computing performance metrics (Sharpe ratio, drawdown, etc.)
- Adding logging and configuration management
- Packaging the project for reuse

---

## Author

Built by Paolo Bordignon as part of a personal deep-dive into quant finance and algorithmic trading.
