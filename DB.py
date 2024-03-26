
import os
import requests
from pinecone import Pinecone

pc = Pinecone(api_key='c4cc0d17-2aa1-43c3-ab41-872383ac35e2')



def get_comp_news(company_name="apple",period="1y"):
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
    