import requests

def Db_check(company_name, period):
    company_name= company_name
    period = period
    query = {
        "company_name":f"{company_name}",
        "period":f"{period}"
    }
    database_url=f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/{company_name}/{period}/Info.json"


    response = requests.get(database_url, params=query)

    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        print("Failed to retrieve data:", response.status_code)

    return data