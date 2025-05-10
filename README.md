# TradeTrack

TradeTrack is a command-line application that helps you track your stock portfolio value in real-time using the Yahoo Finance API.

## Features

- Track multiple stocks in your portfolio
- Real-time stock price updates
- Calculate individual stock values and total portfolio value
- Clean, tabulated output format
- Error handling for invalid tickers

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python tradetrack.py
   ```

2. Enter your stock holdings in the format:
   ```
   Ticker: SYMBOL, Quantity: NUMBER
   ```
   For example:
   ```
   Ticker: AAPL, Quantity: 10
   Ticker: TSLA, Quantity: 5
   ```

3. Press Enter twice when you're done entering stocks

4. The application will display:
   - Current price for each stock
   - Total value for each stock
   - Overall portfolio value

## Example Output

```
Your Portfolio:
+--------+---------------+----------+-------------+
| Ticker | Current Price | Quantity | Total Value |
+========+===============+==========+=============+
| AAPL   | $175.50      | 10       | $1,755.00   |
+--------+---------------+----------+-------------+
| TSLA   | $245.75      | 5        | $1,228.75   |
+--------+---------------+----------+-------------+

Total Portfolio Value: $2,983.75
```

## Features (Planned)
- Input stock tickers and number of shares
- Fetch live stock prices using the yFinance API
- Calculate and display total portfolio value
- Future enhancements: data visualization and historical tracking

## Getting Started
1. Clone the repository:
