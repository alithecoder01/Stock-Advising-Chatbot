from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


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

    functions1 = {
            "name": "get_all_data",
            "description":
            "Get financial data on a specific company for investment purposes",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type":
                        "string",
                        "description":
                        "The name of the company",
                    },
                    "company_ticker": {
                        "type":
                        "string",
                        "description":
                        "the ticker of the stock of the company"
                    },
                    "period": {
                        "type": "string",
                        "description": "The period of analysis"
                    },
                    "filename": {
                        "type": "string",
                        "description": "the filename to store data"
                    }
                },
                "required": ["company_name", "company_ticker"],
            },
        }

    function_call1 = {"name": "get_all_data"}

    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
    model =model.bind(functions= [dict(functions1)],function_call=dict(function_call1))
    
    response = model.invoke(messages).dict()
    
    print(response.get("additional_kwargs")["function_call"])

analyse("amazon")
