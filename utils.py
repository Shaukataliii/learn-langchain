import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from ensure import ensure_annotations

@ensure_annotations
def get_openai_chatmodel(api_key: str = "thisiskey"):
    chatmodel = ChatOpenAI(api_key=api_key)
    return chatmodel

@ensure_annotations
def get_chat_prompt_template(system_role: str):
    prompt_template = ChatPromptTemplate((
        [
            ('system', f"{system_role}"),
            ('user', "{query}")
        ]
    ))
    return prompt_template

@ensure_annotations
def get_openai_llm(api_key: str = "thisiskey"):
    from langchain_openai import OpenAI
    llm = OpenAI(api_key=api_key)
    return llm