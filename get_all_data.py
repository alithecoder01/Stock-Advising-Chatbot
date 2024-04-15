import requests
from get_finc_statment import get_financial_statements
from get_news import get_company_news
from get_stock_evaluation import get_stock_evolution


def get_all_data(company_name, company_ticker, period,today):
    news = get_company_news(company_name, period)

    stock = get_stock_evolution(company_ticker, period)

    statments = get_financial_statements(company_ticker)

    data = {
        "news_results": news,
        "stock_results": stock,
        "statments_results": statments,
    }

    if stock != "No data found":
        database_url = f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/{today}/{company_name}/{period}/Info.json"
        requests.put(database_url, json=data)
    return data
