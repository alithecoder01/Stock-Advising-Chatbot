# 499-Project

### 1. Create a virtual environment using terminal 
```
python3 -m venv .venv
```
### 2. activate virtual environment using terminal 
```
source .venv/bin/activate
```

### 3. install required packages using pip in terminal 
```
pip install requests python-dotenv yfinance yahooquery
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

### 5. Create code that will retrive the news from SERP, click here for resource code [Code](get_news.py)


