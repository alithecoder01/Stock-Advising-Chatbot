from get_finc_statment import get_financial_statements
from get_news import get_comp_news, save_news_txt
from get_stock_evaluation import get_stock_evolution

filePath = "/Users/3lihasan/Desktop/test.txt"
def get_all_data(company_name, company_ticker, period="4y", filename=filePath):
    news = get_comp_news(company_name)
    if news:
        save_news_txt(news, filename)
    else:
        print("No news found.")

    get_stock_evolution(filePath,company_ticker)

    get_financial_statements(company_ticker,filePath)
