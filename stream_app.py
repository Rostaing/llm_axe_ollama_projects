# Method 1
from pandasai.llm.local_llm import LocalLLM 
import streamlit as st
import pandas as pd
from pandasai import Agent

model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

st.title("Data analysis with PandasAI Agent")

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(3))

    agent = Agent(data, config={"llm": model})
    prompt = st.text_input("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(agent.chat(prompt))



# Method 2

from pandasai.llm.local_llm import LocalLLM
import streamlit as st 
import pandas as pd 
from pandasai import SmartDataframe

model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

st.title("Data analysis with PandasAI")

uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(3))

    df = SmartDataframe(data, config={"llm": model})
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(df.chat(prompt))


# Method 3

import streamlit as st 
from langchain_community.llms import Ollama 
import pandas as pd
from pandasai import SmartDataframe

llm = Ollama(model="mixtral")

st.title("Data Analysis with PandasAI")

uploader_file = st.file_uploader("Upload a CSV file", type= ["csv"])

if uploader_file is not None:
    data = pd.read_csv(uploader_file)
    st.write(data.head(3))
    df = SmartDataframe(data, config={"llm": llm})
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(df.chat(prompt))
        else:
            st.warning("Please enter a prompt!")