import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL_PRIORITY = [
    "gemini-2.5-flash-lite"
]

def try_models(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception as e:
        raise Exception(f"Gemini API Error: {e}")

st.title("🧠 Gemini Chat")

user_input = st.text_area("Enter prompt")

if st.button("Ask"):
    if user_input.strip():
        try:
            response = try_models(user_input)
            st.write(response)
        except Exception as e:
            st.error(str(e))
    else:
        st.warning("Enter a prompt first.")