import json
from datetime import date
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from check_data_db import check_data_db
from delete_data import delete_data
from get_all_data import get_all_data


def analyse(request, History):
    messages = [
        SystemMessage(
            content="You are a helpful assistant that find the name of the company and the stock ticker of it and you must give just the company name and the stock ticke. Provide the period needed. If the stock is not available, tell the user that the stock is not found and don't give a response."
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
                    "description": "the period of the data to be analyzed in this form, 1y for one year, 1mo from one month and 1d for one day",
                },
            },
            "required": ["company_name", "company_ticker"],
        },
    }

    function_call = {"name": "get_all_data"}

    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
    model = model.bind(functions=[dict(functions)], function_call=dict(function_call))

    name_ticker_response = model.invoke(messages).dict()

    # To access the values use: response.get("additional_kwargs")["function_call"]

    argument = name_ticker_response.get("additional_kwargs")["function_call"][
        "arguments"
    ]

    # variable (content) to save the feeded up data
    content = ""
    if argument:
        # Parse the arguments from a JSON string to a Python dictionary
        try:
            argument = json.loads(argument)
            company_name = argument["company_name"]
            company_ticker = argument["company_ticker"]
            try:
                period = argument["period"]

            except:
                period = "1mo"
            
        except:
            print("No Data Founded")
        
        today= date.today().day
        # delete the old data from the database
        delete_data(today)
        # check if the data is already in the database
        db_data = check_data_db(company_name, period,today)
        
        if db_data == None:
            content = get_all_data(company_name, company_ticker, period,today)
        else:
            content = db_data

        # gpt-4-0125-preview, the model that we will use to generate the response
        model = ChatOpenAI(model="gpt-3.5-turbo", temperature=1, verbose=True)
        message = [
            SystemMessage(
                content=f"""You are a stock advisor.
                        
                            Answer any question that the user ask.
                        
                            If the User is asking somehting related to a stock do this :
                            Conduct a concise analysis that includes financial data—such as Stock Evolution, balance sheet, cash flow statement, and income statement—and key valuation measures like P/E, P/B ratios, and dividend yield for the company the user asked about.
                            Assess the financial health, operational performance, and market valuation, integrating an evaluation of recent news to identify significant opportunities and risks.
                            Summarize the findings to provide a clear investment recommendation advice, indicating whether investing in the company mentioned is favorable or if caution is advised due to identified risks.
                            Your analysis should offer straightforward investment advice based on the comprehensive evaluation.
                            All the needed information for the analysis are available in {content} .
                            """
            ),
        ]
        for i in range(0, len(History), 2):
            prompt = HumanMessage(content=History[i])
            message.append(prompt)
            response = AIMessage(content=History[i + 1])
            message.append(response)

        prompt = HumanMessage(content=request)
        message.append(prompt)
        respns = model.invoke(message).content
        # print(message)
        return respns
