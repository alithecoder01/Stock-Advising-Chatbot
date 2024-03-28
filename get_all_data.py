import requests
from get_finc_statment import get_financial_statements
from get_news import get_comp_news
from get_stock_evaluation import get_stock_evolution


def get_all_data(company_name, company_ticker, period):
    news = get_comp_news(company_name, period)

    stock = get_stock_evolution(company_ticker, period)

    statments = get_financial_statements(company_ticker)

    data = {
        "news_results": news,
        "stock_results": stock,
        "statments_results": statments,
    }
    database_url = f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/{company_name}/{period}/Info.json"

    requests.put(database_url, json=data)
    return data


