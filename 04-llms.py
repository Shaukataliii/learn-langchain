from utils import get_openai_llm

llm = get_openai_llm()
user_query = input("Enter your query: ")

if user_query != "":
    # llm.invoke(user_query)
    for response_chunk in llm.stream(user_query):
        print(response_chunk)
else:
    print("Invalid input.")