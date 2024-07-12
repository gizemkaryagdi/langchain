from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain_openai import OpenAI
from langchain_community.llms import OpenAI

def query_agent(data,query): # verileri ve sorguyu alan bir fonksiyon oluşturuyoruz. Burada veri CSV verisinden başka bir şey değildir ve sorgu kullanıcıdan gelir.
    df=pd.read_csv(data)
    llm=OpenAI()
    agent=create_pandas_dataframe_agent(llm,df,verbose=True,allow_dangerous_code=True)
    return agent.run(query)
