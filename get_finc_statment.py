from yahooquery import Ticker


# get the company info, like balance sheet and income statment .. ans save them in the .txt file
def get_financial_statements(ticker,filePath):
    # Create a Ticker object
    company = Ticker(ticker)

    # Get financial data
    balance_sheet = company.balance_sheet().to_string()
    # trailing is the Consolidated Cash Flow of the Company during the most recent four fiscal quarters of the Company for which financial statements are available.
    cash_flow = company.cash_flow(trailing=False).to_string()
    income_statement = company.income_statement().to_string()
    valuation_measures = str(company.valuation_measures) 

    # Write data to file
    with open(filePath, "a") as file:
        file.write("\nBalance Sheet\n")
        file.write(balance_sheet)
        file.write("\nCash Flow\n")
        file.write(cash_flow)
        file.write("\nIncome Statement\n")
        file.write(income_statement)
        file.write("\nValuation Measures\n")
        file.write(valuation_measures)
