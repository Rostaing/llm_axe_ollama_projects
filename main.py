from langchain_community.llms import Ollama
# from langchain.document_loaders import CSVLoader
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("factures.csv", encoding="utf-8")
documents = loader.load()

llm = Ollama(model="llama3")

prompt = """il y a combien de factures en 2023"""

data = []
# get content of each document, and add to the data list
for index, doc in enumerate(documents):
    data.append(doc.page_content)

# Concatenate the data list using new-line, and append to the prompt text.
prompt_with_data = prompt + "\n\n" + "\n\n".join(data)

# Execute the prompt using streaming method
for chunks in llm.stream(prompt_with_data):
    print(chunks, end="")