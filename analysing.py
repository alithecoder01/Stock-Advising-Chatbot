from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from get_finc_statment import get_financial_statements
from get_news import get_comp_news, save_news_txt
from get_stock_evaluation import get_stock_evolution

filePath = "/Users/3lihasan/Desktop/test.txt"
def get_all_data(company_name, company_ticker, period="1y", filename=filePath):
    news = get_comp_news(company_name)
    if news:
        save_news_txt(news, filename)
    else:
        print("No news found.")

    get_stock_evolution(filePath,company_ticker)

    get_financial_statements(company_ticker,filePath)


def analyse(request):
    print(f"req conformation: {request}")

    messages = [
        SystemMessage(
            content="You are a helpful assistant that find the name of the company and the stock ticker of it and you must give just the company name and the stock ticker"
        ),
        HumanMessage(
            content=f"Given the user request, what is the comapany name and the company stock ticker ?: {request}?"
        ),
    ]

    functions = {
        "name": "get_all_data",
        "description": "Get financial data on a specific company for investment purposes",
        "parameters": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The name of the company",
                },
                "company_ticker": {
                    "type": "string",
                    "description": "the ticker of the stock of the company",
                },
                "period": {"type": "string", "description": "The period of analysis"},
                "filename": {
                    "type": "string",
                    "description": "the filename to store data",
                },
            },
            "required": ["company_name", "company_ticker"],
        },
    }

    function_call = {"name": "get_all_data"}

    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
    

    response = chat.invoke(messages).dict()
    
    chat.bind_functions(functions= [dict(functions)],function_call=[dict(function_call)])

    print(response.get("content"))

analyse("apple")
