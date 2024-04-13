import requests

def check_data_db(company_name, period,today):
    query = {
        "company_name":f"{company_name}",
        "period":f"{period}"
    }
    # need to change the url to the correct one cc: date to today Variable
    database_url=f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/{today}/{company_name}/{period}/Info.json"

    response = requests.get(database_url, params=query)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None