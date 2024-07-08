# Cookbook for using Hugging Face Hub with Embedchain
# Step-1: Install embedchain package

# !pip install embedchain[huggingface_hub,opensource]

# Step-2: Set Hugging Face Hub related environment variables
# You can find your HUGGINGFACE_ACCESS_TOKEN key on your Hugging Face Hub dashboard

import os
from embedchain import App

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "hf_xxx"

# Step-3 Create embedchain app and define your config
app = App.from_config(config={
    "llm": {
        "provider": "huggingface",
        "config": {
            "model": "google/flan-t5-xxl",
            "temperature": 0.5,
            "max_tokens": 1000,
            "top_p": 0.8,
            "stream": False
        }
    },
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-mpnet-base-v2"
        }
    }
})

# Step-4: Add data sources to your app
app.add("https://www.forbes.com/profile/elon-musk")

# Step-5: All set. Now start asking questions related to your data
while(True):
    question = input("Enter question: ")
    if question in ['q', 'exit', 'quit']:
        break
    answer = app.query(question)
    print(answer)