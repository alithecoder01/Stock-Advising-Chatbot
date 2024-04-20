import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_company_news(company_name, period):
    # params used to structure the request to the API in a way that specifies exactly what information is being sought.
    params = {
        "engine": "google",
        "tbm": "nws",
        "q": company_name,
        "api_key": os.environ["SERPAPI_API_KEY"],
        "period": f"{period}",
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    
    
    return data.get("news_results")

