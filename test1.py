from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage


#simple llm
# llm = OpenAI(openai_api_key=SECRET_KEY)
# response = llm.invoke("Who is prime minister of india")
# print(response)

#chat model
# Example 1
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# response = chat.invoke("Who is prime minister of india")
# print(response.content)

# Example 2
chat = ChatOpenAI(openai_api_key=SECRET_KEY)
messages = [
    SystemMessage(content='You are a standup comedian'),
    HumanMessage(content='who is prime minister of india')
]

response = chat.invoke(messages)
print(response)