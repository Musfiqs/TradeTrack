import yfinance as yf
from tabulate import tabulate
import sys
import time
from datetime import datetime

def get_stock_data(ticker, max_retries=3, delay=1):
    """Fetch stock data for a given ticker with retry logic."""
    for attempt in range(max_retries):
        try:
            print(f"Attempting to fetch data for {ticker} (attempt {attempt + 1}/{max_retries})...")
            stock = yf.Ticker(ticker)
            
            # Add a small delay between requests to avoid rate limiting
            time.sleep(delay)
            
            info = stock.info
            if not info:
                print(f"Warning: No data received for {ticker}")
                continue
                
            current_price = info.get('regularMarketPrice')
            if current_price is None:
                print(f"Warning: No price data available for {ticker}")
                continue
                
            print(f"Successfully fetched price for {ticker}: ${current_price}")
            return current_price
            
        except Exception as e:
            if "429" in str(e) or "Too Many Requests" in str(e):
                wait_time = delay * (attempt + 1)  # Exponential backoff
                print(f"Rate limit hit. Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
                continue
            print(f"Error fetching data for {ticker}: {str(e)}")
            if attempt == max_retries - 1:
                return None
    
    return None

def main():
    print("Welcome to TradeTrack - Your Stock Portfolio Tracker!")
    print("Enter your stock holdings (press Enter twice when done):")
    print("Format: Ticker: SYMBOL, Quantity: NUMBER")
    print("-" * 50)

    portfolio = []
    
    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                break
                
            # Parse the input
            parts = user_input.split(',')
            if len(parts) != 2:
                print("Invalid format. Please use: Ticker: SYMBOL, Quantity: NUMBER")
                continue
                
            ticker_part = parts[0].strip()
            quantity_part = parts[1].strip()
            
            if not ticker_part.startswith("Ticker:") or not quantity_part.startswith("Quantity:"):
                print("Invalid format. Please use: Ticker: SYMBOL, Quantity: NUMBER")
                continue
                
            ticker = ticker_part.replace("Ticker:", "").strip().upper()
            quantity = int(quantity_part.replace("Quantity:", "").strip())
            
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
                
            portfolio.append({"ticker": ticker, "quantity": quantity})
            
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
        except Exception as e:
            print(f"Error processing input: {str(e)}")
    
    if not portfolio:
        print("No stocks entered. Exiting...")
        sys.exit(0)
    
    print("\nFetching current stock prices...")
    print("-" * 50)
    
    # Prepare data for display
    table_data = []
    total_portfolio_value = 0
    
    for holding in portfolio:
        ticker = holding["ticker"]
        quantity = holding["quantity"]
        
        current_price = get_stock_data(ticker)
        
        if current_price is None:
            print(f"Warning: Could not fetch data for {ticker}. This ticker may be invalid.")
            continue
            
        stock_value = current_price * quantity
        total_portfolio_value += stock_value
        
        table_data.append([
            ticker,
            f"${current_price:.2f}",
            quantity,
            f"${stock_value:.2f}"
        ])
    
    # Display the portfolio
    headers = ["Ticker", "Current Price", "Quantity", "Total Value"]
    print("\nYour Portfolio:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")
    print(f"\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 