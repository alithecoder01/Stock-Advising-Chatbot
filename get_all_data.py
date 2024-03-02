from get_finc_statment import get_financial_statements
from get_news import get_comp_news, save_news_txt
from get_stock_evaluation import get_stock_evolution


def get_all_data(company_name, company_ticker, period, filename):
    news = get_comp_news(company_name)
    if news:
        save_news_txt(news, filename)
    else:
        print("No news found.")

    get_stock_evolution(filename,company_ticker,period)

    get_financial_statements(company_ticker,filename)
