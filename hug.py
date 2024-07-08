from embedchain import App
app = App.from_config(config={
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "llama2",
            "temperature": 0.5,
            "top_p": 1,
            "stream": True
        }
    },
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "BAAI/bge-small-en-v1.5"
        }
    }
})

app.add("https://www.forbes.com/profile/elon-musk")
answer = app.query("who is elon musk?")
print(answer)

# while(True):
#     question = input("Enter question: ")
#     if question in ['q', 'exit', 'quit']:
#         break
#     answer = app.query(question)
#     print(answer)