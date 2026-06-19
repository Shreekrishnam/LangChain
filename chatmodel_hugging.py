from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of India?")
print(response.content)