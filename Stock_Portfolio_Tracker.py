import yfinance as yf


def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period='1d')['Close'].iloc[-1]


class StockPortfolio:

    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            self.portfolio[ticker]['quantity'] += quantity
        else:
            self.portfolio[ticker] = {'quantity': quantity, 'price': get_current_price(ticker)}

    def remove_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            if self.portfolio[ticker]['quantity'] >= quantity:
                self.portfolio[ticker]['quantity'] -= quantity
                if self.portfolio[ticker]['quantity'] == 0:
                    del self.portfolio[ticker]
            else:
                print("Not enough shares to remove.")
        else:
            print("Stock not in portfolio.")

    def portfolio_summary(self):
        total_value = 0
        print("Your Stock Portfolio:")
        for ticker, data in self.portfolio.items():
            current_price = get_current_price(ticker)
            stock_value = current_price * data['quantity']
            total_value += stock_value
            print(f"{ticker}: {data['quantity']} shares at ${current_price:.2f} each, Total Value: ${stock_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")


def main():
    portfolio = StockPortfolio()
    while True:
        action = input("What would you like to do? (add/remove/view/exit): ").strip().lower()

        if action == "add":
            ticker = input("Enter stock ticker: ").strip().upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(ticker, quantity)
            print(f"\nAdded {quantity} shares of {ticker}.")

        elif action == "remove":
            ticker = input("Enter stock ticker: ").strip().upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(ticker, quantity)
            print(f"\nRemoved {quantity} shares of {ticker}.")

        elif action == "view":
            portfolio.portfolio_summary()

        elif action == "exit":
            print("Signing Off the portfolio tracker.")
            break

        else:
            print("Invalid action. Please choose 'add', 'remove', 'view', or 'exit'.")


if __name__ == "__main__":
    main()
