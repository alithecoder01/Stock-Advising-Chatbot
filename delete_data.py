import requests

def delete_data(today):
    
    # the url of the database
    database_url = f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/.json"

    # query = {"today": f"{today}"}
    date_check = requests.get(database_url)
    try:
        date_return = date_check.json().keys()
        # convert the dict date to a list
        days = list(date_return)

        for day in days:
            if int(day) < today:
                url_delete = f"https://stock-advisor-9bc47-default-rtdb.europe-west1.firebasedatabase.app/data/{day}.json"
                requests.delete(url_delete)
            elif int(day) == today:
                print("Data today not deleted")
    except:
        print("No data founded")
