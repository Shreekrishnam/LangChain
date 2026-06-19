import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load env
load_dotenv()

# -------------------------
# Gemini Client
# -------------------------
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL_NAME = "gemini-2.5-flash-lite"

# -------------------------
# Load prompt template (FIXED)
# -------------------------
with open("template.json", "r", encoding="utf-8") as f:
    template_str = f.read()

template = PromptTemplate.from_template(template_str)

# -------------------------
# UI
# -------------------------
st.header("🧠 Gemini Chat")

paper_input = st.selectbox(
    "Select a Research Paper Name",
    [
        "Attention is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
        "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"
    ]
)

style_input = st.selectbox(
    "Select a Style",
    ["Beginner Friendly", "Technical", "Code-Oriented", "Creative", "Humorous"]
)

length_input = st.selectbox(
    "Select a Length",
    ["Short", "Medium", "Long"]
)

# -------------------------
# Generate
# -------------------------
if st.button("Generate Summary"):
    chain = template | model=MODEL_NAME | client.models.generate_content
    response = chain.invoke(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )

    st.write(response.text)