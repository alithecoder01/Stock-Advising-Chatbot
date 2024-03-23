import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_comp_news(company_name,period):
    # params used to structure the request to the API in a way that specifies exactly what information is being sought.
    params = {
        "engine": "google",
        "tbm": "nws",
        "q": company_name,
        "api_key": os.environ["SERPAPI_API_KEY"],
        # "date_range": "2023-01-01:2023-01-31",
        "period": f"{period}"
    }
    response = requests.get('https://serpapi.com/search', params=params)
    data = response.json()
    news = data.get('news_results')

    return news



# function for saving the news in .txt file
def save_news_txt(news, filePath):
    with open(filePath, 'w') as file:
        for news_item in news:
            if news_item is not None:
                title = news_item.get('title', 'No title')
                link = news_item.get('link', 'No link')
                date = news_item.get('date', 'No date')
                file.write(f"Title: {title}\n")
                file.write(f"Link: {link}\n")
                file.write(f"Date: {date}\n\n")
