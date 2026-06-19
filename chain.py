import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# -------------------------
# LLM (LangChain wrapper)
# -------------------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# -------------------------
# Prompt
# -------------------------
with open("template.json", "r", encoding="utf-8") as f:
    template_str = f.read()

template = PromptTemplate.from_template(template_str)

# -------------------------
# LCEL CHAIN (YES THIS WORKS)
# -------------------------
chain = template | model

# -------------------------
# UI
# -------------------------
st.header("🧠 Gemini Chat")

paper_input = st.selectbox("Paper", ["Attention is All You Need", "BERT", "GPT-3"])
style_input = st.selectbox("Style", ["Beginner", "Technical"])
length_input = st.selectbox("Length", ["Short", "Medium"])

if st.button("Generate"):

    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(response.content)