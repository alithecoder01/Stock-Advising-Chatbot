import requests
from get_finc_statment import get_financial_statements
from get_news import get_comp_news
from get_stock_evaluation import get_stock_evolution


def get_all_data(company_name, company_ticker, period, filename):
    news = get_comp_news(company_name, period)

    stock = get_stock_evolution(filename, company_ticker, period)

    statement = get_financial_statements(company_ticker, filename)

    data = {'news_results': news, 'stock_results': stock, 'statments_results': statments}
    database_url = f"https://stock-advisor-86cc2-default-rtdb.europe-west1.firebasedatabase.app/data/{company_name}/{period}/info.json"

    requests.put(database_url, json=data)
    return data
