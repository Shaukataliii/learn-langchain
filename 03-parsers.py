from utils import get_openai_chatmodel
from utils import get_chat_prompt_template
from langchain_core.output_parsers.string import StrOutputParser

prompt = get_chat_prompt_template(system_role='You are a world class technical documentation writer.')
llm = get_openai_chatmodel()
parser = StrOutputParser()
chain = prompt | llm | parser

user_query = input("Write code to get its documentation: ")

if user_query != "":
    chain.invoke(input = {"query": f"Write documentation for the code: {user_query}"})
else:
    print("Invalid input.")