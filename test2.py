from decouple import config
from langchain_openai import OpenAI,ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

SECRET_KEY = config('OPENAI_API_KEY')

llm = OpenAI()
# noInputPrompt =PromptTemplate.from_template(template='Tell me a python trick')
oneInputPrompt =PromptTemplate.from_template(template='Tell me a {language} {topic} trick')


formatedInput = oneInputPrompt.format(language = 'python', topic = 'decorator')
response = llm.invoke(formatedInput)

print(response)