from langchain_huggingface import HuggingFaceEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
documents = ["Delhi is the capital of India?", "Mumbai is the financial capital of India.", "Kolkata is known for its cultural heritage."]  

result = embeddings.embed_documents(documents)
print(str(result))
