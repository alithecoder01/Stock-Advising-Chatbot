import yfinance as yf


# function for getting the evaluation of the stock selected
def get_stock_evolution(filePath ,company_name, period="4y"):
    # Get the stock info
    stock = yf.Ticker(company_name)

    # Get historical stock data
    hist = stock.history(period="max")

    # Convert the DataFrame to a string
    data_string = hist.to_string()

    # Append the string to the "test.txt" file
    with open(filePath, "a") as file:
        file.write(f"\nStock Evolution for {company_name}:\n")
        file.write(data_string)
        file.write("\n")
        
