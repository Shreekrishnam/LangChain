from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME']= 'D:/huggingface_cache'
llm= HuggingFacePipeline.from_model_id(
    model_id="sapientinc/HRM-Text-1B",
    
    task="text-generation",
    pipeline_kwargs=dict(
        max_length=2048,
        temperature=0.7,
        max_new_tokens=2048
    )
    
)
model = ChatHuggingFace(llm=llm3)

result = model.invoke("What is the capital of India?")
print(result.content)



