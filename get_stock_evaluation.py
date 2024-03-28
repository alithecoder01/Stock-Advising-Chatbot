import yfinance as yf


# function for getting the evaluation of the stock selected
def get_stock_evolution(company_name, period):
    # Get the stock info
    stock = yf.Ticker(company_name)

    # Get historical stock data
    hist = stock.history(period=period)

    # Convert the DataFrame to a string
    data_string = hist.to_string()

    # Add all the information into one string
    full_text = f"\nStock Evolution for {company_name}:\n"
    full_text = full_text + data_string + "\n"
    return full_text
        
