from yahooquery import Ticker


# get the company info, like balance sheet and income statment .. ans save them in the .txt file
def get_financial_statements(ticker):
    # Create a Ticker object
    company = Ticker(ticker)

    # Get financial data
    try:
        balance_sheet = company.balance_sheet().to_string()
        # trailing is the Consolidated Cash Flow of the Company during the most recent four fiscal quarters of the Company for which financial statements are available.
        cash_flow = company.cash_flow(trailing=False).to_string()
        income_statement = company.income_statement().to_string()
        valuation_measures = str(company.valuation_measures) 
    except:
        balance_sheet= "None"
        cash_flow = "None"
        income_statement = "None"
        valuation_measures = "None"
    
    # Add all the information into one string
    fulltext = (
        "\nBalance Sheet\n"
        + balance_sheet
        + "\nCash Flow\n"
        + cash_flow
        + "\nIncome Statement\n"
        + income_statement
        + "\nValuation Measures\n"
        + valuation_measures
    )
    return fulltext
