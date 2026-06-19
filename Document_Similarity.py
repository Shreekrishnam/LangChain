from langchain_huggingface import HuggingFaceEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents= [
    "Virat Kohli is a famous Indian cricketer.",
    "Sachin Tendulkar is a legendary Indian cricketer.",    
    "MS Dhoni is a former captain of the Indian cricket team.",
    "Rohit Sharma is a talented Indian batsman.",
    "Jasprit Bumrah is a skilled Indian fast bowler.",
    "Anushka Sharma is a popular Bollywood actress."
]

query ='tell me about Sharma, the actress'

doc_embeddings= embeddings.embed_documents(documents)
query_embedding= embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

sorted_scores = sorted(
    list(enumerate(scores)),
    key=lambda x: x[1],
    reverse=True
)

index, score = sorted_scores[0]
print(query)
print(documents[index])
print("similarity score: ", score)