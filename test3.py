from decouple import config
from langchain_openai import OpenAI,ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

SECRET_KEY = config('OPENAI_API_KEY')

chat = OpenAI()


# chatPrompt = ChatPromptTemplate.from_messages([
#     ("system","You are a helpful assistant that translate {input_language} to the {output_language}."),
#     ("human","{text}")])

# formattedChatPrompt = chatPrompt.format_messages(
#     input_language = 'english',
#     output_language = 'hindi',
#     text = 'what is your name and your father name')

# response = chat.invoke(formattedChatPrompt)
# print(response)

sys_template = "You are a helpful assistant that translate {input_language} to the {output_language}."
human_template = "{text}"

chatPrompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(sys_template),
    HumanMessagePromptTemplate.from_template(human_template)
])


formattedChatPrompt = chatPrompt.format_messages(
    input_language = 'english',
    output_language = 'hindi',
    text = 'What is your name')


response = chat.invoke(formattedChatPrompt)

print("RESPONSE",response)

