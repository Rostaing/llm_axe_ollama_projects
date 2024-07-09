# # Method 2

# from pandasai.llm.local_llm import LocalLLM
# import streamlit as st 
# import pandas as pd 
# from pandasai import SmartDataframe
# from dotenv import load_dotenv
# import os
# from langchain_groq.chat_models import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model_name="llama3-70b-8192", 
#     api_key = os.environ["GROQ_API_KEY"])

# st.title("Data analysis with PandasAI")

# uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=['csv'])

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file,  encoding='ISO-8859-1') # encoding='ISO-8859-1'
#     st.write(data.head())

#     df = SmartDataframe(data, config={"llm": llm})
#     prompt = st.text_input("Enter your prompt:")

#     if st.button("Generate"):
#         if prompt:
#             with st.spinner("Generating response..."):
#                 st.write(df.chat(prompt))


# from langchain_community.llms import Ollama
# # from langchain.document_loaders import CSVLoader
# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader("titanic.csv", encoding="utf-8")
# documents = loader.load()

# llm = Ollama(model="llama3")

# prompt = """il y a combien passagers"""

# data = []
# # get content of each document, and add to the data list
# for index, doc in enumerate(documents):
#     data.append(doc.page_content)

# # Concatenate the data list using new-line, and append to the prompt text.
# prompt_with_data = prompt + "\n\n" + "\n\n".join(data)

# # Execute the prompt using streaming method
# for chunks in llm.stream(prompt_with_data):
#     print(chunks, end="")

from llm_axe import OnlineAgent, OllamaChat, PdfReader
llm = OllamaChat(model="llama3:instruct")

pdfReader = PdfReader(llm)
resp = pdfReader.ask("De quoi parle ce document et a qui appartient cela ?", ["facture.pdf"])
# onlineAgent = OnlineAgent(llm)

# resp = onlineAgent.search(resp + "\n What is his nationality about?")
print(resp)
