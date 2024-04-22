# 499-Project

### 1. Create a virtual environment using terminal 
```
python3 -m venv .venv
```
### 2. Activate virtual environment using terminal 
```
source .venv/bin/activate
```

### 3. Install required packages using pip in terminal 
```
pip install requests python-dotenv yfinance yahooquery langchain-openai Flask "Flask[async]
```

> [!IMPORTANT]
> In the YF files in utils.py update this code to avoid FutureWarning  
>```
>From df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
>To df.index += _pd.to_timedelta(dst_error_hours, 'h')
>```

### 4. Create .env file to save the api keys 
```
OPENAI_API_KEY="Your Key"
SERPAPI_API_KEY="Your Key"
```

### 5. Create code that will retrieve the news from SERP, click here for resource code [Code](get_news.py)

### 6. Create code that retrieves the evaluation of the stock selected, click here for resource code [Code](get_stock_evaluation.py)

### 7. Create code that gets the company info, balance sheet etc .. , click here for resource code [Code](get_finc_statment.py)

### 8. Create code that adds all the 3 methods together, click here for resource code [Code](get_all_data.py)

### 9. Create code for getting the company name, ticker and the respons, click here for resource code [Code](main.py)

### 10. Create code for checking if the data exist in DB or not, click here for resource code [Code](check_data.py)

### 11. Create code for deleting the old data exist in DB, click here for resource code [Code](delete_data.py)




