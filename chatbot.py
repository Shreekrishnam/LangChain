import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

chat_history = [
    SystemMessage(content="You are an expert AI research assistant.")
]

while True:
    user_input= input('You: ')
    chat_history.append(HumanMessage(content=user_input))  

    if user_input == 'exit':
        break
    result = model.invoke(chat_history )
    chat_history.append(AIMessage(content=result.content))  
    print("Gemini: " + result.content)


   
print(chat_history)   

