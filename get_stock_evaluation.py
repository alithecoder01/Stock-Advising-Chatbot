import yfinance as yf


# function for getting the evaluation of the stock selected
def get_stock_evolution(company_ticker, period):
    # Get the stock info
    stock = yf.Ticker(company_ticker)

    # Get historical stock data
    hist = stock.history(period=period)

    if hist.empty:
        return "No data found"
    # Convert the DataFrame to a string
    data_string = hist.to_string()

    # Add all the information into one string
    full_text = f"\nStock Evolution for {company_ticker}:\n"
    full_text = full_text + data_string + "\n"
    return full_text
