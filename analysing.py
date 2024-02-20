from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def analyse(request):
    print(f"req conformation: {request}")

    chat = ChatOpenAI(model="gpt-3.5-turbo",temperature=1)

    messages = [
        SystemMessage(
            content="You are a helpful assistant that find the name of the company and the stock ticker of it and you must give just the company name and the stock ticker"
        ),
        HumanMessage(
            content=f"Given the user request, what is the comapany name and the company stock ticker ?: {request}?"
        )
    ]
    
