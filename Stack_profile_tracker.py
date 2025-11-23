# Predefined stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 145,
    "MSFT": 310
}

print("=== STOCK PORTFOLIO TRACKER ===\n")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

portfolio = {}
total_investment = 0

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    elif stock in stock_prices:
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            investment = qty * stock_prices[stock]
            portfolio[stock] = investment
            total_investment += investment
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found in the list.")

print("\n--- Portfolio Summary ---")
for s, value in portfolio.items():
    print(f"{s}: ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (y/n): ").lower()
if save == "y":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for s, value in portfolio.items():
            f.write(f"{s}: ${value}\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print("Portfolio saved as 'portfolio_summary.txt'")
