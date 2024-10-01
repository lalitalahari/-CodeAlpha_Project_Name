# Placeholder for portfolio data
portfolio = {}

# Function to add a stock to the portfolio
def add_stock():
    stock_symbol = input("Enter stock symbol: ").upper()
    quantity = int(input(f"How many shares of {stock_symbol} do you own? "))
    purchase_price = float(input(f"At what price did you buy {stock_symbol}? "))

    # Add stock details to the portfolio
    portfolio[stock_symbol] = {'quantity': quantity, 'purchase_price': purchase_price}
    print(f"{quantity} shares of {stock_symbol} added at ${purchase_price:.2f} each.\n")

# Function to remove a stock from the portfolio
def remove_stock():
    stock_symbol = input("Enter stock symbol to remove: ").upper()

    if stock_symbol in portfolio:
        del portfolio[stock_symbol]
        print(f"{stock_symbol} removed from your portfolio.\n")
    else:
        print(f"{stock_symbol} not found in your portfolio.\n")

# Function to track performance of the portfolio
def track_portfolio():
    if not portfolio:
        print("Your portfolio is empty.\n")
        return
    
    print("\n--- Stock Portfolio ---")
    total_value = 0

    for stock_symbol, details in portfolio.items():
        quantity = details['quantity']
        purchase_price = details['purchase_price']
        current_price = float(input(f"Enter the current price of {stock_symbol}: "))

        # Calculate performance
        current_value = quantity * current_price
        profit_loss = (current_price - purchase_price) * quantity

        total_value += current_value

        print(f"\n{stock_symbol}:")
        print(f"  Quantity: {quantity} shares")
        print(f"  Purchase Price: ${purchase_price:.2f}")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Current Value: ${current_value:.2f}")
        print(f"  Profit/Loss: ${profit_loss:.2f}")
    
    print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")

# Main function to handle user options
def portfolio_manager():
    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            track_portfolio()
        elif choice == '4':
            print("Exiting the portfolio manager.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the stock portfolio manager
if __name__ == "__main__":
    portfolio_manager()
