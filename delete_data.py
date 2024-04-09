from datetime import date
import requests


def delete_data(company_name, period):
    today = date.today().day
    
    database_url = f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/{today}/{company_name}/{period}/Info.json"

    query = {
        "today": f"{today}"
    }
    date_check = requests.get(database_url, params=query)
    date_return = date_check.json().get("date")

    if date_return == today:
        print("Data found")
    else:
        print("Data not found")



    # response = requests.delete(database_url)
    # if response.status_code == 200:
    #     print("Data deleted")
    # else:
    #     print("Data not found")

    # r = requests.get(
    #     "https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/json"
    # )
    # print(r.json())

delete_data("Apple", "1M")